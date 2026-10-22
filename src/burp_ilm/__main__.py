import signal, sys
if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
from .cli import main
sys.exit(main())
