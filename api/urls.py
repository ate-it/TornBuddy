from django.urls import re_path

from loot.views import LootApiView

urlpatterns = [
    re_path("loot/", LootApiView.as_view()),
]
