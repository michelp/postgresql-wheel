# postgresql-wheel

A Python wheel for Linux containing a locally installable PostgreSQL
database server.

All servers run as the Python process user in a local path, so this
wheel does not require root or sudo privledges.

Servers can be setup and torn down in test fixtures with no additional
outside dependencies.

Currently this wheel only works for most flavors of Linux.  MacOS and
maybe even Windows are doable... by someone else.

Postgres is compiled in the same "manylinux" environments provided by
the [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/)
tool using [Github Actions]() and directly archived into the wheel's "package_data".

The wheel can be installed with pip:

```
$ pip install postgresql-wheel
```

```py3
>>> import postgresql, psycopg2
>>> postgresql.initdb(D="testdatabase")                        # initialize a local database
>>> postgresql.pg_ctl("start", D="testdatabase", o="-p 5456")  # start local database

>>> c = psycopg2.connect("postgres://localhost:5456/postgres") # connect with local client
In [6]: with c.cursor() as q:
   ...:     q.execute("select version()")
   ...:     print(q.fetchall())
   ...: 
   ...: 
[('PostgreSQL 13.4 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 8.3.1 20190311 (Red Hat 8.3.1-3), 64-bit',)]

```

