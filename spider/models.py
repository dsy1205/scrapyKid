from django.db import models

# Create your models here.

from django.db import models


class Message(models.Model):
    url_root = models.URLField(max_length=100, verbose_name="初始地址")
    url_goal = models.URLField(max_length=500, verbose_name="最终的爬取地址")
    spider_message = models.TextField(max_length=500)
    html_message = models.TextField(max_length=500)
    gmt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_goal.encode("utf-8")

class BaggageInfo(models.Model):
    depart = models.CharField(max_length=3, verbose_name="出发地")
    destinent = models.CharField(max_length=3, verbose_name="抵达地")
    baggage_message = models.TextField(max_length=500)
    url = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.baggage_message

