from django.urls import path
from . import views

urlpatterns = [
    path("bikes/", views.BikeListView.as_view(), name="bikes"),
    path("bikes/<int:pk>/", views.BikeDetailView.as_view(), name="bike"),
    path(
        "order/<int:pk>/",
        views.OrderDetailView.as_view(),
        name="order"
    )
]
