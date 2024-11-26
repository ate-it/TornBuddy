from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

from loot.views import LootApiView

from . import views

schema_view = get_swagger_view(title="TornBuddy")
urlpatterns = [
    path("", views.index),
    re_path("loot/", LootApiView.as_view()),
]
