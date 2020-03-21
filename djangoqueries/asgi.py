"""
ASGI config for Django Queries project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# fmt: off
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoqueries.settings")  # noqa
# fmt: on
application = get_asgi_application()
