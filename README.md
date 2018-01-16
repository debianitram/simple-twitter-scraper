Simple Twitter Scraper
======================


# Requerimientos

* Python 3.4, 3.5
* Django>=2
* python-twitter
* celery
* djangorestframework (opcional)


# Instalación

Instalando usando `pip`:

    pip install git+https://github.com/debianitram/simple-twitter-scraper.git

Agregar `'twitter_scraper'` en las `INSTALLED_APPS` de la configuración de tu proyecto.

```python
INSTALLED_APPS = (
    ...
    'twitter_scraper',
)
```

Necesitas crear las credenciales para usar la api de twitter y añadirlas en el settings de tu proyecto Django.
Para mayor detalle visita `Twitter OAuth <https://dev.twitter.com/oauth/overview>`_

```python
TW_CONSUMER_KEY = ''
TW_CONSUMER_SECRET = ''
TW_ACCESS_TOKEN_KEY = ''
TW_ACCESS_TOKEN_SECRET = ''
```

Agregar url a las urlpatterns de tu proyecto Django en el archivo urls.py

```python
urlpatterns = [
    ...
    path('twitter_scraper/', include('twitter_scraper.urls')),
]
```

## Aplicar las migraciones.

``` bash
python manage.py migrate
```

## Iniciar el worker
```bash
$ celery -A proj worker -l info
```

## Call API.

```bash
$ # call API djangorestframework
$ curl -X POST http://dominio/twitter_scraper/drf_api/profiles/ -d query=facebook

$ # call API
$ curl -X POST http://dominio/twitter_scraper/api/profiles/ -d query=twitter
```



