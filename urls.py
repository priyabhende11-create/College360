from django.urls import path
from . import views

urlpatterns = [
    path("principal_login/", views.principal_login, name="principal_login"),
    path("principal_dashboard/", views.principal_dashboard, name="principal_dashboard"),
]