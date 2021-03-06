Technical requirements
======================

The Aristotle Metadata Registry is built on the Django framework which supports a wide range of
operating systems and databases. While Aristotle-MDR should support most of these
only a small set of configurations have been thoroughly tested on the
`Travis-CI <https://travis-ci.org/aristotle-mdr/aristotle-metadata-registry/>`_
continuous integration systems as "supported infrastucture".

Operating system support
------------------------

* Ubuntu Linux (Precise Pangolin) 12.04 LTS (verification courtesy of Travis-CI)

Travis-CI does not yet have containerised support for the Ubuntu 14.04 or 16.04
long-term support releases.

Python
------
Only the latest releases of Python are supported. New users are recommended to use Python 3.5 or above.

* Python 3.5+

Django
------

* Django version 1.11 LTS


Database support
----------------

* SQLite
* Postgres
* MariaDB

Notes:

Aristotle has been tested against Microsoft SQL Server 2016 on Windows, but we
no longer provide official testing against this database.

MySQL has issues incompatible with Aristotle that prevent it from being used.
Consider using an alternative like MariaDB if you need MySQL-like support.

Search index support
--------------------

* Elasticsearch 5.0+ (Only tested on Linux)
* Whoosh (Linux and Windows)
