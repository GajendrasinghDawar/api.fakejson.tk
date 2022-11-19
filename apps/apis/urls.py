from django.urls import path 
from .views import PostsList, PostDetail, ListImage, UsersList, UserDetail,StateList, DistrictList, api_root,StateDetail 
from .views import  ListImage,StateList, DistrictList, api_root,StateDetail

urlpatterns = [
    path('', api_root, name='api_root'),
]

urlpatterns += [
    path('posts/', PostsList.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view()),
]

urlpatterns += [
    path('users/', UsersList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(),name='users-detail'),
]

urlpatterns += [
    path('states/', StateList.as_view(), name='states'),
    path('states/<int:pk>/', StateDetail.as_view(), name='states'),
    path('districts/', DistrictList.as_view(), name='districts'),
]

urlpatterns += [
    path('images/', ListImage.as_view(), name='images'),
]
