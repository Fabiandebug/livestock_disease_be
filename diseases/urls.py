from django.urls import path, include
from .views import diseaseListView, imageListView, diseaseIdentifiers

# URL Parttens
urlpatterns = [
    # API Views URLS
    path("disease/", diseaseListView.as_view(), name="diseaseListView"),
    # <str:identifier>/<str:language>
    path(
        "disease/<str:identifier>/<str:language>",
        diseaseListView.as_view(),
        name="diseaseListViewUpdateDelete",
    ),
    path(
        "disease/identifiers/", diseaseIdentifiers.as_view(), name="disease-identifiers"
    ),
    path("image/", imageListView.as_view(), name="imageListView"),
    path("image/<int:pk>/", imageListView.as_view(), name="imageListView"),
]
