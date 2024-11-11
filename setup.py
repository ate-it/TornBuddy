import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TornBuddy.settings")

django.setup()
from django.contrib.auth.models import User  # noqa: E402

cmd = "python manage.py reset_db"
r = os.system(cmd)

cmd = "python manage.py migrate"
r = os.system(cmd)

cmd = "npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css"
r = os.system(cmd)

print("create superuser")
User.objects.create_superuser("admin", "admin@example.com", "adminpass")
