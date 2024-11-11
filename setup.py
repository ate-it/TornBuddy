import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TornBuddy.settings")
print("------------------")

django.setup()
from django.contrib.auth.models import User

cmd = "python manage.py reset_db"
r = os.system(cmd)

cmd = "python manage.py migrate"
r = os.system(cmd)

if not len(User.objects.all()):
    print("create superuser")
    User.objects.create_superuser("admin", "admin@example.com", "adminpass")
