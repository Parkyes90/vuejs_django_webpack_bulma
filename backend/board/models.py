from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('TITLE', max_length=50, null=False)
    country = CountryField(blank_label='(select country)', null=True)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    content = models.TextField('CONTENT', null=False)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='upload/%Y/%m/%d/orig')
    filtered_image = models.ImageField(blank=True, null=True,
                                       upload_to='upload/%Y/%m/%d/filtered')

    # category = models.ForeignKey(Categories)
    class Meta:
        app_label = 'board'
        db_table = 'POST'

    def __str__(self):
        return self.title

        # def get_absolute_url(self):
        # return reverse('korea:post_detail', args=(self.id,))

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Post, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:post_detail', args={self.id})


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments')
#     user = models.ForeignKey(User)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     approved_comment = models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.message
#
#     class Meta:
#         ordering = ('created_at',)
