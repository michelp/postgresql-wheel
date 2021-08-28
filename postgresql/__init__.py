from pathlib import Path

from plumbum import local
import postgresql

local.env.path.append(Path(postgresql.__file__).parent / "bin")

initdb = local.cmd.initdb
pg_ctl = local.cmd.pg_ctl

from . import _version
__version__ = _version.get_versions()['version']
