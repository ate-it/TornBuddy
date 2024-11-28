from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from loot.views import LootApiView

schema_view = get_schema_view(
    openapi.Info(
        title="TornBuddy API",
        default_version="v1",
        url="https://tornbuddy.com/api/",
        description="API Endpoints for TornBuddy",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path("loot/", LootApiView.as_view()),
]
