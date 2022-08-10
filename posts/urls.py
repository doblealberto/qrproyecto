"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),
   

    path(
        route='posts/new/',
        view=views.CreateMausoleoView.as_view(),
        name='create'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
     path(
        route='posts/qr/<int:pk>',
        view=views.QRView.as_view(),
        name='qr'
    ),
]
