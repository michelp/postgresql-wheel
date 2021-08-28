# postgresql-wheel

A Python wheel for Linux containing the entire PostgreSQL database
server.

The wheel can be installed with pip:

```
$ pip install postgresql-wheel
```

This wheel contains a complete PostgreSQL database server, compiled on
the same "manylinux" platforms provided by the cibuildwheel tool and
directly archived into the wheel's "package_data".  All servers run as
the Python process user so this wheel does not require root or sudo
privledges.

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

