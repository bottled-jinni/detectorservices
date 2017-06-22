from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import BotSerializer, NodeSerializer
from .models import Bot, Node

class BotViewSet(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
