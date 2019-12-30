"""
ASGI config for asgi_channel_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asgi_channel_demo.settings')

application = get_asgi_application()

from . import settings
if settings.DEBUG:
    import ptvsd
    ptvsd.enable_attach(address=('127.0.0.1', 3000), redirect_output=True)

    # Pause the program until a remote debugger is attached
    ptvsd.wait_for_attach()