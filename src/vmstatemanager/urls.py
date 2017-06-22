from django.conf.urls import url
from django.views.generic import TemplateView
from .api import BotViewSet, NodeViewSet
from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
#urlpatterns = [
#    url(r'^bots$', BotViewSet()),
#    url(r'^nodes$',NodeViewSet()),
#    url(r'^', TemplateView.as_view(template_name="vmstatemanager/index.html")),
#]

router = DefaultRouter()
router.register(r'bots',  BotViewSet)
router.register(r'nodes', NodeViewSet)
#router.register(r'', TemplateView.as_view(template_name="vmstatemanager/index.html"))

urlpatterns = router.urls
