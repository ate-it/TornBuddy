import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TornBuddy.settings")

django.setup()
from django.contrib.auth.models import User  # noqa: E402

from loot.models import NPC  # noqa: E402

cmd = "python manage.py reset_db"
r = os.system(cmd)

cmd = "python manage.py migrate"
r = os.system(cmd)


print("create superuser")
User.objects.create_superuser("admin", "admin@example.com", "adminpass")

# NPC's
print("Create NPC's")
NPC.objects.create(torn_id=4, visible=True)  # Duke
NPC.objects.create(torn_id=15, visible=True)  # Leslie
NPC.objects.create(torn_id=10, visible=False)  # Scrooge
NPC.objects.create(torn_id=19, visible=True)  # Jimmy
NPC.objects.create(torn_id=20, visible=True)  # Fernando
NPC.objects.create(torn_id=21, visible=True)  # Tiny
