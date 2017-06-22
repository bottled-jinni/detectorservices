from rest_framework import serializers
from .models import Bot, Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__' 


class BotSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(read_only=True, many=True)
    class Meta:
        model = Bot
        fields = '__all__' 







