# -*- coding: utf-8 -*-
import time
from ..models import Post

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def get_time(request):
    return Response((int(time.time())))


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def list_up(request):
    post = Post.objects.order_by('-create_date').values_list(
        'id', 'title', 'country', 'content', 'create_date', 'user', 'image', 'filtered_image'
    )

    data = []

    for id, title, country, content, create_date, user, image, filtered_image in post:
        data.append({
            'id': id,
            'title': title,
            'country': country,
            'content': content,
            'create_date': create_date,
            'user': user,
            'image': image,
            'filtered_image': filtered_image
        })

    return Response({'success': True, 'totalCount': len(data), 'data': data})
