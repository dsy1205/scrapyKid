from django.db import models

# Create your models here.

from django.db import models


class message(models.Model):
    url_root = models.CharField(max_length=100)
    url_goal = models.CharField(max_length=500)
    spider_message = models.CharField(max_length=500)
    html_message = models.CharField(max_length=500)
    gmt_time = models.DateTimeField(max_length=6)
