from subprocess import check_output
from pathlib import Path
import postgresql

pg_bin = Path(postgresql.__file__).parent / "bin"


def initdb(cmdline):
    cmdline = str(pg_bin / "initdb") + " " + cmdline
    return check_output(cmdline, shell=True)


def pg_ctl(cmdline):
    cmdline = str(pg_bin / "pg_ctl") + " " + cmdline
    return check_output(cmdline, shell=True)


from . import _version

__version__ = _version.get_versions()["version"]
