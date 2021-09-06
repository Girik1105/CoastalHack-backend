from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/', views.create_community, name="community-create"),
    path('list/', views.list_community, name="community-list"),
    path('edit/<str:slug>/', views.edit_community, name="community-edit"),
    path('delete/<str:slug>/', views.delete_community, name="community-delete"),
]