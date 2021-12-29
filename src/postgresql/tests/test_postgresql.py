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


def test_postgis_extension(tmp_postgres):
    pgdata, con_str = tmp_postgres
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION postgis;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION postgis_raster;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION postgis_topology;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION postgis_sfcgal;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION fuzzystrmatch;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION address_standardizer;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION address_standardizer_data_us;"')
    postgresql.psql(f'-d "{con_str}" -c "CREATE EXTENSION postgis_tiger_geocoder;"')
