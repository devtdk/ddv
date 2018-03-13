from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TypeSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        # example of field error exception (in specific validate method)
        if value[0] == '5':
            raise serializers.ValidationError("Nazwa nie może rozpoczynać się cyfrą 5")
        return value

    def validate(self, data):

        # example of non-field-errors exception
        if data['name'][0] == '1':
            raise serializers.ValidationError("Nazwa nie może rozpoczynać się cyfrą 1")

        # example of field error exception (in general validate)
        if data['name'][0] == '2':
            raise serializers.ValidationError({ 'name': "Nazwa nie może rozpoczynać się cyfrą 2"})

        return data

    class Meta:
        model = models.Type
        fields = '__all__'
