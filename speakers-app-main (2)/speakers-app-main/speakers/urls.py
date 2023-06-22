from django.urls import path
from . import views

urlpatterns = [
    path("", views.speakers_list, name="speakers_list"),
    path("<int:pk>/", views.speaker_detail, name="speaker_detail"),
    path("<int:pk>/update/", views.speaker_update, name="speaker_update"),
    path("<int:pk>/delete/", views.speaker_delete, name="speaker_delete"),
]
