"""
ASGI config for resume_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from django.core.management import execute_from_command_line
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume_app.settings")
application = get_asgi_application()

if len(sys.argv) > 1 and sys.argv[1] == "serve":
    execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:8080"])
