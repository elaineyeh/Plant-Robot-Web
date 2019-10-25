"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy

from mainsite.views import index, register, edit, operation

from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetView,
                                       PasswordResetConfirmView)


password_change_parms = dict(
    template_name='registration/password_change.html',
    success_url=reverse_lazy('login'),
)

password_reset_parms = dict(
    template_name='registration/password_reset.html',
    subject_template_name='registration/password_reset_subject.txt',
    email_template_name='registration/password_reset_email.html',
    html_email_template_name='registration/password_reset_html_email.html',
    success_url=reverse_lazy('login')
)

password_reset_confirm_parms = dict(
    template_name='registration/password_reset_confirm.html',
    post_reset_login=True,
    success_url=reverse_lazy('login')
)

urlpatterns = [
    path('', index, name='index'),
    path('operation/', operation, name='operation'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('todo/', include('todo.urls')),
    path('password-change/',
         PasswordChangeView.as_view(**password_change_parms),
         name='password_change'),
    path('password-reset/', PasswordResetView.as_view(**password_reset_parms),
         name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(**password_reset_confirm_parms),
         name='password_reset_confirm'),
]

if not getattr(settings, "GCP", False):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
