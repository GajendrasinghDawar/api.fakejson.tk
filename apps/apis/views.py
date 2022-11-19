import random
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User, State, District, Post, Image
from .serializers import UserSerializer, StateSerializer, StateDetailSerializer, DistrictSerializer, PostSerializer, ImageSerializer
from .pagination import DistrictResultsSetPagination


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('posts', request=request, format=format),
        'users': reverse('users', request=request, format=format),
        'states': reverse('states', request=request, format=format),
        'districts': reverse('districts', request=request, format=format),
        'images': reverse('images', request=request, format=format),
    })


class PostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StateList(generics.ListAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class StateDetail(generics.RetrieveAPIView):
    serializer_class = StateDetailSerializer
    queryset = State.objects.all()


class DistrictList(generics.ListAPIView):
    serializer_class = DistrictSerializer
    pagination_class = DistrictResultsSetPagination
    queryset = District.objects.all()


def pick_random_object():
    return random.randrange(1, Image.objects.all().count() + 1)


class ListImage(generics.ListAPIView):
    serializer_class = ImageSerializer
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return Image.objects.all().filter(id=pick_random_object())
