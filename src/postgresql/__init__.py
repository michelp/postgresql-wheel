import sys
import os
import shutil
from subprocess import check_output
from pathlib import Path
from tempfile import TemporaryDirectory
from time import sleep
import pytest

pg_bin = Path(__file__).parent / "bin"


def prog(name):
    def f(cmdline):
        cmdline = str(pg_bin / name) + " " + cmdline
        return check_output(cmdline, shell=True)

    return f


progs = """
clusterdb          ecpg               pg_checksums       pg_dumpall         pg_restore         pg_verifybackup    reindexdb
createdb           initdb             pg_config          pg_isready         pg_rewind          pg_waldump         vacuumdb
createuser         pg_archivecleanup  pg_controldata     pg_receivewal      pg_test_fsync      postgres
dropdb             pg_basebackup      pg_ctl             pg_recvlogical     pg_test_timing     postmaster
dropuser           pgbench            pg_dump            pg_resetwal        pg_upgrade         psql
""".split()


__all__ = ["setup", "teardown", "tmp_postgres"]

this = sys.modules[__name__]
for p in progs:
    setattr(this, p, prog(p))
    __all__.append(p)


def setup(pgdata=None, log="db_test.log", user="postgres"):
    if pgdata is None:
        pgdata = TemporaryDirectory()

    log = Path(log)
    try:
        log.unlink()
    except FileNotFoundError:
        pass

    initdb(f"-D {pgdata.name} --auth-local=trust --no-sync -U postgres")
    pg_ctl(f'-D {pgdata.name} -o "-k {pgdata.name} -h \\"\\"" -l {log} start')
    sleep(3)
    con_str = f"host={pgdata.name} user={user}"
    return pgdata, con_str


def teardown(pgdata):
    msg = pg_ctl(f"-D {pgdata.name} stop")
    pgdata.cleanup()
    return msg


@pytest.fixture
def tmp_postgres():
    pgdata, con_str = setup()
    yield pgdata, con_str
    teardown(pgdata)


from . import _version

__version__ = _version.get_versions()["version"]
