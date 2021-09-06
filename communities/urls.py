from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/', views.create_community, name="community-create"),
    path('list/', views.list_community, name="community-list"),
    path('edit/<str:slug>/', views.edit_community, name="community-edit"),
    path('delete/<str:slug>/', views.delete_community, name="community-delete"),

    path('<str:slug>/members/', views.add_remove_members, name="member-management"),

    path('<str:slug>/posts/create/', views.create_community_posts, name="community-posts-create"),
    path('<str:slug>/posts/list/', views.list_community_posts, name="community-posts-list"),
    path('<str:slug>/posts/<int:pk>/delete/', views.delete_community_posts, name="community-posts-delete"),
]