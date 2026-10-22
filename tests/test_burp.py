import json, os, subprocess, sys, pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = dict(os.environ, PYTHONPATH=str(ROOT / "src"))
C = '#include <stdio.h>\n/* binary search in a sorted array */\nint binary_search(int values[], int count, int key) {\n  int low = 0, high = count - 1;\n' \
    '  while (low <= high) { int middle = low + (high - low) / 2;\n    if (values[middle] == key) return middle;\n' \
    '    if (values[middle] < key) low = middle + 1; else high = middle - 1; }\n  return -1;\n}\nint main(void) { int values[] = {2, 5, 8};\n' \
    '  printf("%d\\n", binary_search(values, 3, 8)); return 0; }\n'
Y = '%{\n#include <stdio.h>\nint yylex(void); void yyerror(const char *msg) { fprintf(stderr, "%s\\n", msg); }\n%}\n%token NUM\n%left \'+\'\n%%\n' \
    'input: | input line ;\nline: \'\\n\' | expr \'\\n\' { printf("%d\\n", $1); } ;\nexpr: NUM | expr \'+\' expr { $$ = $1 + $3; } ;\n%%\n'


def burp(*a):
    return subprocess.run([sys.executable, "-m", "burp_ilm", *map(str, a)], capture_output=True, text=True, env=ENV)


def test_version_and_help_carry_the_notices():
    for args in (["--version"], ["--help"]):
        out = burp(*args).stdout
        assert "© 1993–2026 Abhishek Choudhary. All rights reserved." in out and "MIT" in out and "trademark" in out


def test_languages():
    langs = burp("languages").stdout.split()
    assert len(langs) >= 70 and "urdu" in langs and "hindi" in langs


def test_ingest_translates_names_and_comments_and_reverses_exactly(tmp_path):
    src = tmp_path / "src"; src.mkdir(); (src / "search.c").write_text(C); (src / "calc.y").write_text(Y)
    r = burp("ingest", src, "--langs", "urdu,tamil,hindi", "--out", tmp_path / "out", "--translators", "glossary")
    assert r.returncode == 0, r.stdout + r.stderr
    progress = [json.loads(l[14:]) for l in r.stdout.splitlines() if l.startswith("BURP-PROGRESS ")]
    assert {p["lang"] for p in progress} == {"urdu", "tamil", "hindi"}
    urdu = (tmp_path / "out/urdu/search.c").read_text(encoding="utf-8")
    assert "ثنائی_تلاش" in urdu and "binary_search" not in urdu and "ترتیب شدہ صف میں ثنائی تلاش" in urdu
    tamil_y = (tmp_path / "out/tamil/calc.y").read_text(encoding="utf-8")
    assert "%token" in tamil_y and "%left" in tamil_y                     # a grammar's own directives stay as they are
    assert (tmp_path / "out/GAPS.md").exists() and json.loads((tmp_path / "out/GAPS.json").read_text())["languages"]
    for lang in ("urdu", "tamil", "hindi"):
        back = tmp_path / "back" / lang
        assert burp("reverse", tmp_path / "out" / lang, "--out", back).returncode == 0
        for f in ("search.c", "calc.y"):
            assert (back / f).read_bytes() == (src / f).read_bytes(), (lang, f)


def test_unsupported_languages_are_reported(tmp_path):
    src = tmp_path / "src"; src.mkdir(); (src / "a.c").write_text("int main(void) { return 0; }\n"); (src / "b.rs").write_text("fn main() {}\n")
    r = burp("ingest", src, "--langs", "urdu", "--out", tmp_path / "out")
    assert r.returncode == 0
    assert json.loads((tmp_path / "out/GAPS.json").read_text())["files_in_languages_burp_cannot_read"] == {".rs": 1}


def test_a_single_file_is_ingested_and_comes_back(tmp_path):
    f = tmp_path / "search.c"; f.write_text(C)
    r = burp("ingest", f, "--langs", "urdu", "--out", tmp_path / "out")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ثنائی_تلاش" in (tmp_path / "out/urdu/search.c").read_text(encoding="utf-8")
    assert burp("reverse", tmp_path / "out/urdu", "--out", tmp_path / "back").returncode == 0
    assert (tmp_path / "back/search.c").read_bytes() == f.read_bytes()
    c = burp("check", f, "--langs", "urdu,tamil")
    assert c.returncode == 0 and "2 reverse to the original byte for byte" in c.stdout, c.stdout


def test_a_missing_path_or_an_empty_project_is_an_error_never_a_silent_nothing(tmp_path):
    assert burp("ingest", tmp_path / "nowhere", "--langs", "urdu", "--out", tmp_path / "o").returncode != 0
    (tmp_path / "empty").mkdir()
    r = burp("ingest", tmp_path / "empty", "--langs", "urdu", "--out", tmp_path / "o")
    assert r.returncode != 0 and "no files" in r.stderr


def test_build_systems_follow_renamed_files_and_come_back_exactly(tmp_path):
    src = tmp_path / "proj"; src.mkdir(); (src / "search.c").write_text(C)
    build = {"Makefile": "CFLAGS = -DVERBOSE\nsearch: search.c\n\tcc $(CFLAGS) -o search search.c\n",
             "CMakeLists.txt": "add_executable(search search.c)\nadd_definitions(-DVERBOSE)\n",
             "meson.build": "executable('search', 'search.c')\n", "Kconfig": "config SEARCH\n\tbool \"search\"\n",
             "configure.ac": "AC_INIT([search], [1.0])\nAC_CONFIG_SRCDIR([search.c])\n", "BUILD.bazel": "cc_binary(name = \"search\", srcs = [\"search.c\"])\n"}
    for name, text in build.items():
        (src / name).write_text(text)
    r = burp("ingest", src, "--langs", "urdu", "--out", tmp_path / "out", "--rename-files")
    assert r.returncode == 0, r.stdout + r.stderr
    renamed = [p.name for p in (tmp_path / "out/urdu").glob("*.c")]
    assert renamed and renamed[0] != "search.c"
    for name in ("Makefile", "CMakeLists.txt", "meson.build", "configure.ac", "BUILD.bazel"):
        text = (tmp_path / "out/urdu" / name).read_text(encoding="utf-8")
        assert renamed[0] in text and "search.c" not in text, name          # the build follows the renamed file
    gaps = json.loads((tmp_path / "out/GAPS.json").read_text())
    assert not gaps["files_in_languages_burp_cannot_read"]                    # build files are read, not merely copied
    assert burp("reverse", tmp_path / "out/urdu", "--out", tmp_path / "back").returncode == 0
    for p in src.iterdir():
        assert (tmp_path / "back" / p.name).read_bytes() == p.read_bytes(), p.name
