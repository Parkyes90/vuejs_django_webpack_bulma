# -*- coding: utf-8 -*-
from pandas.io import json
from django.http import HttpResponse


def json_encode(func):
    def decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        response = json.dumps(response)
        resp = HttpResponse(response, content_type="application/json")
        resp.flush()
        return resp
