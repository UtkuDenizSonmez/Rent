from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.home, name="home"),
    path("success/", views.ContactSuccessView.as_view(), name="success"),
]
