from django.urls import path, include
from .views import diseaseListView, imageListView

# URL Parttens
urlpatterns = [
    # API Views URLS
    path("disease/", diseaseListView.as_view(), name="diseaseListView"),
    path(
        "disease/<str:identifier>/<str:language>/",
        diseaseListView.as_view(),
        name="diseaseListViewUpdateDelete",
    ),
    path("image/", imageListView.as_view(), name="imageListView"),
    path("image/<int:pk>/", imageListView.as_view(), name="imageListView"),
]
