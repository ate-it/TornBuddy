from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:faction_id>", views.view_faction, name="View Faction"),
    path("<int:faction_id>/members", views.faction_members, name="Faction Members"),
]
