# postgresql-wheel

A Python wheel for Linux containing a complete, self-contained,
locally installable PostgreSQL database server.

All servers run as the Python process user in a local path, so this
wheel does not require root or sudo privledges.  Databases can be
initialized in any directory.

Servers can be setup and torn down in test fixtures with no additional
outside dependencies.

Currently this wheel only works for most flavors of Linux.

Postgres is compiled in the same "manylinux" environments provided by
the [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/)
tool using [Github
Actions](https://github.com/michelp/postgresql-wheel/blob/main/.github/workflows/wheels.yml)
and directly archived into the wheel's "package_data".

The wheel can be installed with pip:

```
$ pip install postgresql-wheel
```

Postgres binaries in the package can be found in the directory pointed
to by the `postgresql.pg_bin` global variable.  Function wrappers
around all of the postgres binary programs, like `initdb` and `pg_ctl`
functions are provided for convenience:

```py3
>>> from postgresql import initdb, pg_ctl
>>> initdb('-D testdatabase')
>>> pg_ctl('-D testdatabase -o "-p 5678" -l testdatabase.log start')

>>> import psycopg2
>>> c = psycopg2.connect("postgres://localhost:5678/postgres") # connect with local client
>>> with c.cursor() as q:
>>>     q.execute("select version()")
>>>     print(q.fetchall())
...
[('PostgreSQL 13.4 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 8.3.1 20190311 (Red Hat 8.3.1-3), 64-bit',)]
>>> pg_ctl('-D testdatabase stop)

```

For the purposes of testing, convenience functions are provided for
setting up and tearing down databases:

```py3
>>> pgdata, con_str = postgresql.setup()
>>> postgresql.psql(f'-h {con_str} -c "select version()"')
>>> postgresql.teardown(pgdata)
```

There is also a pytest fixture called `tmp_postgres` that returns a
new connection string to a temporary databse local domain socket, and
can be used in a pytest:

```py3
>>> from postgresql import tmp_postgres
>>> def test_foo(tmp_postgres):
...    postgresql.psql(f'-h {tmp_postgres} -c "select version()")
```

