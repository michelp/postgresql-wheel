import postgresql


def test_setup_teardown():
    pgdata, conn = postgresql.setup()
    postgresql.teardown(pgdata)
