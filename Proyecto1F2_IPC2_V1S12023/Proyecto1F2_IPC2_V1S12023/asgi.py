"""
ASGI config for Proyecto1F2_IPC2_V1S12023 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto1F2_IPC2_V1S12023.settings')

application = get_asgi_application()
