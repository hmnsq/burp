# BURP

**Put source code into a human language, and back, byte for byte, and say what is still missing.** BURP does one thing,
ingestion, at every size: a single file, a whole project, and the project's build system. Keywords come from each language's
tables, names and comments from each language's dictionary. The build files (make, automake, CMake, Meson, autoconf, Kconfig,
SCons, Bazel, Ninja, qmake, GN and Android's) follow the project: the names they pass with `-D` and, with `--rename-files`,
the file names they mention. `burp reverse` brings everything back to the original, byte for byte. Every ingestion writes
`GAPS.md`: the names with no dictionary entry, the comments not yet translated, the keywords a language's table lacks, the
names that collided, and the files in languages BURP cannot read yet.

```
pipx install burp-ilm
burp ingest ./my-project --langs urdu,tamil --out ./in-languages     # a project, with its build system
burp ingest ./search.c --langs urdu --out ./in-urdu                     # a single file
burp reverse ./in-languages/urdu --out ./back            # identical to ./my-project
burp languages
```

BURP ingests; [paras](https://github.com/hmnsq/paras) carries the same BURP inside it and does the rest: it takes any free
software, forks it, has BURP ingest it into every language, keeps only the languages that come back exactly, publishes them,
and reports what to do next. The language tables come from the canonical Hindawi, hindawiai/hindawi2026.10 (2026.10.11).

| Claim | State |
|---|---|
| Ingestion into 76 languages and the round trip back, byte for byte | verified (tests; xv6 in all 76 languages) |
| A single file, and build systems following renamed files, back exactly | verified (tests) |
| Dictionaries for names and comments | 43 languages, proposed words for review by their speakers |

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. MIT licence (the original Hindawi tables keep theirs: NOTICE).
BURP™ and Hindawi™ are his trademarks.
