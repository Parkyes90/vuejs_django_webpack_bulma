# -*- coding: utf-8 -*-
from django.views.generic import View as BaseView
from django.shortcuts import redirect


class View(BaseView):
    def dispatch(self, request, method, *args, **kwargs):
        if not method:
            method = 'index'

        handler = getattr(self, method, self.method_not_found)
        return handler(request, *args, **kwargs)

    def method_not_found(self, request, *args, **kwargs):
        return redirect("/")

# EOF