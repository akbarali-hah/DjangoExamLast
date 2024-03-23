from django.core.mail import send_mail
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductPriceFilterSet
from apps.models import Category, Product, User
from apps.pagination import CustomPageNumberPagination
from apps.permissions import IsOwnerOrReadOnly
from apps.serializers import RegisterModelSerializer, CategoryModelSerializer, ProductModelSerializer, \
    ProductUpdateModelSerializer, Task1Serializer, Task2Serializer
from root.settings import EMAIL_HOST_USER


class CategoryAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    filter_backends = SearchFilter,
    filterset_fields = 'name',


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    filter_backends = [SearchFilter]
    filterset_fields = 'name'
    search_fields = 'name', 'description',

    def update(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return Response('You are not owner !!!')
        return super().update(request, *args, **kwargs)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        email_subject = 'Django-Exam'
        email_message = 'You have successfully registered!'
        send_mail(email_subject, email_message, EMAIL_HOST_USER, [user.email])


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'name',
    pagination_class = CustomPageNumberPagination


class ProductListApiView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = 'name', 'description',
    pagination_class = CustomPageNumberPagination


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductUpdateModelSerializer
    queryset = Product.objects.all()
    permission_classes = IsAuthenticated, IsOwnerOrReadOnly


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductUpdateModelSerializer
    queryset = Product.objects.all()
    permission_classes = IsAuthenticated, IsOwnerOrReadOnly


class Task1APIView(GenericAPIView):
    serializer_class = Task1Serializer

    def post(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Tekshirildi!'})


class Task2APIView(ListAPIView):
    serializer_class = Task2Serializer
    queryset = Product.objects.all()
    filter_backends = SearchFilter,
    search_fields = 'name', 'description'
    pagination_class = None

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.filter_queryset(self.queryset), many=True)
        return Response(serializer.data, status=201)


class Task3APIView(ListAPIView):
    serializer_class = Task2Serializer
    queryset = Product.objects.all()
    filter_backends = DjangoFilterBackend,
    filter_class = ProductPriceFilterSet
    pagination_class = None
