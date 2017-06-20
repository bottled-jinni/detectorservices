from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Bot(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Bot: {}".format(self.name)


@python_2_unicode_compatible
class Node(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    infected    = models.BooleanField(default=True)
    bot         = models.ForeignKey(Bot, related_name="nodes")
    random      = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Node: {}".format(self.name)
