from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    author = models.ManyToManyField(User, through='Varet', related_name='comm')



    class Meta:
        ordering = ['created']




class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    posts = models.ForeignKey('Post', related_name='categorie', blank=True, on_delete=models.CASCADE)
    #posts_1 = models.ManyToManyField('Post', through='Varet', blank=True)


    class Meta:
        verbose_name_plural = 'categories'




class  Varet(models.Model):
    name = models.IntegerField()
    posts = models.ForeignKey('Post', related_name='categories', blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='got', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name}'


class  Art(models.Model):
    name = models.ForeignKey('Post', related_name='cat', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'






