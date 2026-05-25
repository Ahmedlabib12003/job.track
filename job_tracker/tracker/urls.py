from django.urls import path
from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.dashboard.as_view(), name="dashboard"),
    path("new/", views.create.as_view(), name="create"),
    path("<int:pk>/edit/", views.update.as_view(), name="update"),
]
