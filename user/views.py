from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

from .models import User
from .serializers import UserSerializer
import jwt


# API User
@api_view(['GET', ])
def api_detail_user(request, id_user):
    try:
        user = User.objects.get(id=id_user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)


# get all User in databases
@api_view(['GET', ])
def api_all_user(request):
    user = User.objects.all()
    if request.method == "GET":
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


# update one user
@api_view(['PUT', ])
def api_update_user(request, id_user):
    try:
        user = User.objects.get(id=id_user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = UserSerializer(user, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful !"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_user(request, id_user):
    try:
        user = User.objects.get(id=id_user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = user.delete()
        data = {}
        if operation:
            data["success"] = "Delete successful !"
        else:
            data["failure"] = "Delete failed !"
        return Response(data=data)


@api_view(['POST', ])
def api_create_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_login(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = User.objects.get(username=data["username"])
            if user.verifify_password(data["password"]):
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', ])
def api_get_jwt(request):
    data = {}
    if request.method == 'POST':
        try:
            data = request.data
            user = User.objects.get(username=data['username'])
            if user.verifify_password(data['password']):
                encoded_jwt = jwt.encode(request.data, settings.SECRET_KEY,
                                         algorithm='HS256')
                return Response(data={'token': encoded_jwt})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
