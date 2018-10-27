# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.permissions import SafeMethodsPermission
from api.serializers import LinkSerializer
from core.models import Link


class URLViewSet(ModelViewSet):
    # Modelviewset which create, updates Link
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (SafeMethodsPermission,)

