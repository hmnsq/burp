"""BURP: the bidirectional ingestion of source code into human languages, and back, byte for byte.
© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Licensed under the MIT licence (see LICENSE and NOTICE)."""
from pathlib import Path

__version__ = "2026.10.0"
HOME = Path(__file__).parent
BURP = HOME / "burp" / "burp.py"
GLOSSARY = HOME / "burp" / "glossary"
NOTICE = (f"BURP {__version__}\n"
          "© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.\n"
          "Licensed under the MIT licence. The original Hindawi tables it carries (upstream/chintamani) keep their own licence; see NOTICE.\n"
          "BURP™ and Hindawi™ are trademarks of Abhishek Choudhary.\n"
          "Source and citation: https://github.com/hmnsq/burp (CITATION.cff).")


def languages():
    """Every language BURP has tables for."""
    return sorted({d.name for d in (HOME / "languages").iterdir() if (d / "c2h.uhin").exists()} | {"hindi"})
