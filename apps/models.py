import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, ImageField, DateTimeField, \
    EmailField, UUIDField, PositiveIntegerField


class User(AbstractUser):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = CharField(max_length=255, null=True, blank=True)
    last_name = CharField(max_length=255, null=True, blank=True)
    email = EmailField(max_length=255, unique=True)


class Category(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    description = TextField(max_length=255)
    price = PositiveIntegerField(default=0)
    category = ForeignKey('apps.Category', CASCADE)
    owner = ForeignKey('apps.User', CASCADE)

    def __str__(self):
        return self.name


class ProductPhoto(Model):
    user = ForeignKey('apps.Product', CASCADE)
    image = ImageField(upload_to='users', blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
