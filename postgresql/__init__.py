import sys
from subprocess import check_output
from pathlib import Path

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


this = sys.modules[__name__]
for p in progs:
    setattr(this, p, prog(p))


from . import _version

__version__ = _version.get_versions()["version"]
