# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator

from ..models import Post
from first.view import View
from ...deco import json_encode
# Create your views here.


class BoardView(View):
    @method_decorator(json_encode)
    def listup(self, request):
        return self._listup(request)

    def _listup(self, request):
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

        return {'success': True, 'totalCount': len(data), 'data': data}
