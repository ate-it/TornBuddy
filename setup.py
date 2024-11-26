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
NPC.objects.create(torn_id=4, name="Duke", visible=True)  # Duke
NPC.objects.create(torn_id=7, name="Amanda", visible=False)
NPC.objects.create(torn_id=10, name="Scrooge", visible=False)  # Scrooge
NPC.objects.create(torn_id=15, name="Leslie", visible=True)  # Leslie
NPC.objects.create(torn_id=17, name="Easter Bunny", visible=False)  # Leslie
NPC.objects.create(torn_id=19, name="Jimmy", visible=True)  # Jimmy
NPC.objects.create(torn_id=20, name="Fernando", visible=True)  # Fernando
NPC.objects.create(torn_id=21, name="Tiny", visible=True)  # Tiny

print("Debug: Starting Loot Update")
NPCs = NPC.objects.all()
for npc in NPCs:
    npc.update()
print("Debug: Ending Loot Update")
