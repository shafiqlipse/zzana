from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("confirm/", Confirm, name="confirm"),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('success/', success, name='success'),
    path("change_password/", change_password, name="change_password"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    
    # miscellaneous=================================
    path("notice/<int:id>", Notice_detail,name="notice_detail"),
    path("noticeboard/", Notices,name="notices"),
    path("complaints/", Complaints,name="complaints"),
    path("visitors/", Visitors,name="visitors")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
