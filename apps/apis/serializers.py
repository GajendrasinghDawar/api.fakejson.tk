from .models import Post, Image
from rest_framework import serializers, relations
from rest_framework.relations import StringRelatedField
from .models import User, State, District


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        repr = super(PostSerializer, self).to_representation(instance)
        repr['user'] = instance.user.name
        return repr


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class StateDetailSerializer(serializers.ModelSerializer):
    districts = serializers.StringRelatedField(many=True)

    class Meta:
        model = State
        fields = ['id', 'state_name', 'districts']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

    def to_representation(self, instance):
        repr = super(DistrictSerializer, self).to_representation(instance)
        repr['state'] = instance.state.state_name
        return repr


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
