# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.permissions import SafeMethodsPermission
from api.serializers import UserEmailSerializer
from core.models import UserEmail


class URLViewSet(ModelViewSet):
    # Modelviewset which create, updates Link
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer
    permission_classes = (SafeMethodsPermission,)
