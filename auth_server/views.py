import random

from django.shortcuts import render
from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, renderers

from .models import AuthenticationLog

class CustomBasicAuthentication(BasicAuthentication):
    
    www_authenticate_realm = 'auth'


class AuthView(APIView):
    """
    Returns 200 if an active User exists for the 
    given basic auth request.  Otherwise, returns 
    the appropriate HTTP error code. 
    """
    authentication_classes = (CustomBasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [renderers.JSONRenderer]

    def get(self, request, format=None):
        content = {}
        headers = {'Cache-Control':"no-cache, no-store, must-revalidate", 
                   "Pragma":'no-cache'}
        http_status=status.HTTP_200_OK
        user = request.user
        content.update({
        'user': str(user),  # `django.contrib.auth.User` instance.
        })
        
        AuthenticationLog.objects.record(user.username, request)
        
        return Response(content, status=http_status, headers=headers)
