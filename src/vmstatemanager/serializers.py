from rest_framework import serializers

from .models import Bot, Node


class BotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bot
        fields = '__all__' 


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = '__all__' 

