from rest_framework.generics import ListAPIView

from .serializers import BotSerializer, NodeSerializer
from .models import Bot, Node

class BotApi(ListAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class NodeApi(ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
