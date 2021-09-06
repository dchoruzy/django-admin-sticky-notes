from django.urls import path
from django_admin_sticky_notes.views import StickyNoteView


urlpatterns = [
    path("", StickyNoteView.as_view()),
]
