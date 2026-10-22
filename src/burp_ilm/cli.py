"""burp: put source code into a human language, and back, byte for byte; and say what is still missing.
© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Licensed under the MIT licence (see LICENSE and NOTICE)."""
import runpy, sys
from . import BURP, NOTICE, languages

HELP = """burp: put source code into a human language, and back, byte for byte.

  burp ingest <folder> --langs urdu,tamil --out <folder>     into each language; GAPS.md says what is still missing
  burp reverse <language folder> --out <folder>               back to the original, byte for byte
  burp check <folder> --langs urdu                            ingest, reverse and compare, without keeping anything
  burp languages                                              every language BURP has tables for

  ingest options: --translators glossary[,argos,llm,cmd]  --rename-files  --jobs N  (burp ingest --help for all)
"""


def main(argv=None):
    import signal
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)      # piped into head or less, it ends quietly, as Unix tools do
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv[:1] in (["--version"], ["-V"], ["version"]):
        print(NOTICE); return 0
    if not argv or argv[:1] in (["-h"], ["--help"], ["help"]):
        print(HELP); print(NOTICE); return 0
    if argv[0] == "languages":
        print(" ".join(languages())); return 0
    sys.argv = ["burp", *argv]
    try:
        runpy.run_path(str(BURP), run_name="__main__")
    except SystemExit as e:
        if isinstance(e.code, str):                       # BURP's own message for why it stopped: always shown
            print(e.code, file=sys.stderr)
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    return 0
