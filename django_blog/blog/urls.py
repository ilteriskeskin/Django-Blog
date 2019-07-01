from django.urls import path
from .views import post_list, post_create, post_update, post_delete

urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('update/', post_update, name='update'),
    path('delete/', post_delete, name='delete'),
]