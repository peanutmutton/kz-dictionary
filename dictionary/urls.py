from django.urls import path

from .views import index_view, word_detail_view

urlpatterns = [
    path("", index_view, name="index"),
    path("<str:word>/", word_detail_view),
]