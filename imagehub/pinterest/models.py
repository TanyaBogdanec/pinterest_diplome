from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name_user = models.CharField(max_length=100, verbose_name='name_user')
    email = models.EmailField(max_length=150, verbose_name='email')
    password = models.CharField(max_length=10)


class Image(models.Model):
    file = models.ImageField()
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delete = models.BooleanField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

