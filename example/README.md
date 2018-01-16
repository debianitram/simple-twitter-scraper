Demo Simple Twitter Scraper
===========================


Requeriments
============

Debian 9
--------
* python3
* python3-dev
* python-virtualenv
* virtualenvwrapper.
* python3-pip
* redis-server

Instalación
===========

Descargar la demo:
```bash
$ cd /tmp/
$ svn export https://github.com/debianitram/simple-twitter-scraper/trunk/example
```

Crear entorno virtual:

```bash
$ cd example/
$ mkvirtualenv demo --python=$(which python3)
```

Instalar requerimientos del proyecto:

```bash
(demo)$ pip install -r requirements.txt
```

Cambiar las siguientes configuraciones en el settings de la demo.
```python
# Config Twitter API
TW_CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)
TW_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', None)
TW_ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY', None)
TW_ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', None)
```

Inicializar la base de datos:

```bash
(demo)$ ./manage.py migrate
```


Inciar servidor de desarrollo:
```bash
(demo)$ python manage.py runserver
```

Iniciar Worker
```bash
(demo)$ celery -A project worker -l info
```


