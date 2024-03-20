from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, CharField, EmailField, Serializer, IntegerField

from apps.models import Category, Product, User


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name',


class ProductModelSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = 'uuid', 'name', 'description', 'price', 'owner'


class RegisterModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    email = EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError('Email already exists!')
        return value

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            return data
        raise ValidationError("Password doesn't match!")


class ProductUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'name', 'description', 'price'


class Task1Serializer(Serializer):
    group_id = IntegerField(default=100)
    student_id = IntegerField(default=15)


class Task2Serializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'uuid', 'name', 'description', 'price'
