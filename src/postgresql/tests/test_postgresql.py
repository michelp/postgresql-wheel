import postgresql
from postgresql import tmp_postgres


def test_setup_teardown():
    pgdata, conn = postgresql.setup()
    postgresql.teardown(pgdata)


def test_fixture(tmp_postgres):
    pgdata, con_str = tmp_postgres
    postgresql.psql(f'-d "{con_str}" -c "select version()"')


def test_default_extension(tmp_postgres):
    pgdata, con_str = tmp_postgres
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION hstore;"')


def test_uuid_ossp_extension(tmp_postgres):
    pgdata, con_str = tmp_postgres
    postgresql.psql(f'-d "{con_str}" -c \'CREATE EXTENSION "uuid-ossp";\'')


def test_xml2_extension(tmp_postgres):
    pgdata, con_str = tmp_postgres
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION xml2;"')
