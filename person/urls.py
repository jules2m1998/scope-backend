from django.urls import path
from person import views

urlpatterns = [
    path('<id_person>', views.api_detail_person, name="detail"),
    path('', views.api_all_person, name="all"),
    path('<id_person>/update', views.api_update_person, name="update"),
    path('create', views.api_create_person, name="create"),
    path('<id_person>/delete', views.api_delete_person, name="delete"),
    path('image/<int:id_image>', views.api_detail_image, name="imageDetail"),
    path('all/image', views.api_all_image, name="imageAll"),
    path('image/person/<int:id_person>', views.api_all_person_image, name="personImageDetail"),
    path('image/<id_image>/update', views.api_update_image, name="updateImage"),
    path('image/<id_image>/delete', views.api_delete_image, name="deleteImage"),
    path('image/create/<id_person>', views.api_create_image, name="createImage"),
]