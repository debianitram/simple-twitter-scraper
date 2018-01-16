from rest_framework import serializers

from . import models


class TwitterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TwitterProfile
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('query', )