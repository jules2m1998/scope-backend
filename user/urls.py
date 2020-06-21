from django.urls import path
from user import views


urlpatterns = [
    path('', views.api_all_user, name="all"),
    path('<id_user>', views.api_detail_user, name="detail"),
    path('<id_user>/update', views.api_update_user, name="update"),
    path('create/', views.api_create_user, name="create"),
    path('<id_user>/delete', views.api_delete_user, name="delete"),
    path('login/', views.api_login, name="delete"),
]