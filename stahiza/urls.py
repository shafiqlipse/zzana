from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from client.views import Home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home, name="home"),
    path("auth/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("students/", include("students.urls")),
    path("people/", include("human_resource.urls")),
    path("library/", include("library.urls")),
    path("classes/", include("classes.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
