from subprocess import check_output
from pathlib import Path
import postgresql

pg_bin = Path(postgresql.__file__).parent / "bin"


def initdb(*args, **kwargs):
    args.insert(pg_bin / "initdb", 0)
    return check_output(*args, **kwargs)


def pg_ctl(*args, **kwargs):
    args.insert(pg_bin / "pg_ctl", 0)
    return check_output(*args, **kwargs)


from . import _version

__version__ = _version.get_versions()["version"]
