# django3

## prepare env

```bash
pip install -r requirements
#to start
daphne asgi_channel_demo.asgi:application
#if with nginx in socket
daphne -u /tmp/daphne.sock django_project.asgi:application
#use supervisor
daphne --fd 5 django_project.asgi:application
# https, only support HTTP/2 when using TLS,
pip install -U Twisted[tls,http2]
daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem django_project.asgi:application
```

## socket io, channel

[ ref ] (https://channels.readthedocs.io/en/latest/)

## WARNING websocket is not support,  from github issue list

https://github.com/django/daphne/issues/292  
https://github.com/dimkoug/celeryproject

## this can work, but not able to be used in production

python manage.py runserver

## also this is useful page

https://www.tutorialdocs.com/tutorial/django-channels/asgi.html