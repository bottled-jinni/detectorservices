from django.conf.urls import url

from .api import BotApi, NodeApi

urlpatterns = [
    url(r'^bots$', BotApi.as_view()),
    url(r'^nodes$', NodeApi.as_view())

]
