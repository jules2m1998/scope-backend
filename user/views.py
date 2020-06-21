from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from passlib.hash import pbkdf2_sha256


# API User
@api_view(['GET', ])
def api_detail_user(request, id_user):
    try:
        user = User.objects.get(id=id_user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserSerializer(User)
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
    user = User.objects.create()
    if request.method == "POST":
        data = request.data
        data['password'] = pbkdf2_sha256.encrypt(data['password'], rounds=12000, salt_size=32)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_login(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        try:
            user = User.objects.get(username=data["username"])
            if user.verifify_password(data["password"]):
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)


def _hash(pwd):
    return make_password(pwd)
