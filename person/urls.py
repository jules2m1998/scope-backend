from django.urls import path
from person import views

urlpatterns = [
    path('<id_person>', views.api_detail_person, name="detail"),
    path('', views.api_all_person, name="all"),
    path('<id_person>/update', views.api_update_person, name="update"),
    path('create', views.api_create_person, name="create"),
    path('<id_person>/delete', views.api_delete_person, name="delete"),
]