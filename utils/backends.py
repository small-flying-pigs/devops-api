#!/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time: 2020/9/27 12:42
@Author: yu.jiang <safemonitor@outlook.com>
@License: Apache License
@File: backends.py

"""

from django.contrib.auth.backends import ModelBackend
from api.models import UserInfo
from django.db.models import Q


class MobileOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
