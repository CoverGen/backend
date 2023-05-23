from django.urls import path
from .events import EventApiView

urlpatterns = [
    path("", EventApiView.as_view()),
]
