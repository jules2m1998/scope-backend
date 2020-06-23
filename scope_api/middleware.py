import json

import jwt
from django.conf import settings

from user.models import User
from rest_framework import status
from django.http import HttpResponse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info.lstrip('/')
        paths = ['user/register/',
                 'user/jwt/',
                 'user/login/',
                 'person/create/',
                 'person/all/image',
                 'individual/create/',
                 'person/image/find']
        jwt_token = request.headers.get('authorization', None)
        if path in paths:
            return None
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, settings.SECRET_KEY,
                                     algorithm='HS256')
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return HttpResponse(json.dumps({'message': 'Token is invalid'}),
                                    content_type="application/json",
                                    status=status.HTTP_404_NOT_FOUND)
            try:
                user = User.objects.get(username=payload['username'])
                return None
            except User.DoesNotExist:
                return HttpResponse(json.dumps({'message': 'Token is invalid'}),
                                    content_type="application/json",
                                    status=status.HTTP_404_NOT_FOUND)
        return HttpResponse(json.dumps({'message': "token not exist"}), content_type="application/json",
                            status=status.HTTP_404_NOT_FOUND)
