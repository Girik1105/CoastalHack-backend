from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, user_list

urlpatterns = [
    path('', user_list.as_view(), name="list-users"),
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]