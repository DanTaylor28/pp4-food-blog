from django.urls import path
# from . import views
from .views import HomeView, PostView, AddView, UpdatePostView, DeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', PostView.as_view(), name='post_view'),
    path('create/post/', AddView.as_view(), name='create_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', DeleteView.as_view(), name='delete_post'),
]
