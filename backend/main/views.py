# coding=utf-8
from django.shortcuts import render

from first.view import View
# Create your views here.


class BaseView(View):
    def index(self, request, context=None):
        return render(
            request,
            'index.html',
            context
        )
