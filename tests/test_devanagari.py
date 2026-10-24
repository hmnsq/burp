"""A Devanagari language comes out wholly Devanagari: every name and comment of the project's own, whatever no translator
gives being spelt; and it still reverses byte for byte. © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI."""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = '''/* compute the sum of a vector */
#include <stdio.h>
double vector_sum(double *values, int count) {
    double total = 0.0;   // running total
    for (int k = 0; k < count; k++) total += values[k];
    return total;
}
int main(void) { double xs[3] = {1, 2, 3}; printf("%f\\n", vector_sum(xs, 3)); return 0; }
'''


def test_sanskrit_is_wholly_devanagari_and_reverses(tmp_path):
    src = tmp_path / "src"; src.mkdir(); (src / "sum.c").write_text(SRC, encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-m", "burp_ilm", *a], capture_output=True, text=True,
                                    env={"PYTHONPATH": str(ROOT / "src"), "PATH": "/usr/bin:/bin"})
    r = run("ingest", str(src), "--langs", "sanskrit", "--out", str(tmp_path / "out"), "--translators", "glossary")
    assert r.returncode == 0, r.stdout + r.stderr
    text = (tmp_path / "out/sanskrit/sum.c").read_text(encoding="utf-8")
    code = re.sub(r'"(?:[^"\\]|\\.)*"', '""', text)
    left = set(re.findall(r"[A-Za-z][A-Za-z0-9]*", code)) - {"stdio", "h", "printf"}
    assert not left, left
    r = run("reverse", str(tmp_path / "out/sanskrit"), "--out", str(tmp_path / "back"))
    assert r.returncode == 0 and (tmp_path / "back/sum.c").read_text(encoding="utf-8") == SRC
