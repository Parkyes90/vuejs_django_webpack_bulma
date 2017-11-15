# -*- coding: utf-8 -*-
import time
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from ..models import Post
from first.view import View
from ...deco import json_encode
# Create your views here.


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def get_time(request):
    return Response((int(time.time())))
