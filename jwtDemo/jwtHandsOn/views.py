# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from calendar import timegm
from datetime import datetime

import jwt
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from jwtHandsOn.serializers import *


# def jwt_response_payload_handler(token, user=None, request=None):
#     # to be implemented
#     return {'token':token}

def jwt_payload_handler(user):
    return {
        'username':user.username,
        'user_id':user.pk,
        'email':user.email,
        'myf':1,
        'exp':datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'orig_iat': timegm(
            datetime.utcnow().utctimetuple()
        )
    }


@api_view(['GET','POST'])
def foo(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    tokenPayload = jwt.decode(token,None,None)
    if request.method == 'POST':
        return Response({"your data":request.data})
    return Response({"your data":"GEAR UP"})


@api_view(['GET','POST'])
@authentication_classes(())
@permission_classes(())
def foobar(request):
    if request.method == 'POST':
        return Response({"your unsafe data":request.data})
    return Response({"your data":"STEP UP"})


@api_view(['POST'])
@permission_classes(())
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)