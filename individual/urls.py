from django.urls import path
from individual import views


urlpatterns = [
    path('', views.api_all_individual, name="all"),
    path('<id_individual>', views.api_detail_individual, name="detail"),
    path('<id_individual>/update', views.api_update_individual, name="update"),
    path('create/', views.api_create_individual, name="create"),
    path('<id_individual>/delete', views.api_delete_individual, name="delete"),
]