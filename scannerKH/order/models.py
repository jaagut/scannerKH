from django.db import models
from article.models import Article
from wholesaler.models import Wholesaler
from user.models import User
from datetime import datetime


class Position(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return f"ARTICLE: ({self.article.__str__()}), QUANTITY: {self.quantity}"

class Order(models.Model):
    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.PROTECT)
    create_user = models.ForeignKey(User, related_name='create', on_delete=models.DO_NOTHING)
    create_stamp = models.DateTimeField(default=datetime.now)
    modified_user = models.ForeignKey(User, related_name='modified', on_delete=models.DO_NOTHING)
    modified_stamp = models.DateTimeField(auto_now=True)
    transmit_user = models.ForeignKey(User, related_name='transmit', on_delete=models.DO_NOTHING)
    transmit_stamp = models.DateTimeField(blank=True, null=True)
    positions = models.ManyToManyField(Position)

    def __str__(self):
        return f"WHOLESALER: ({self.wholesaler.__str__()}), CREATE: {self.create_stamp.__str__()}, MODIFIED: {self.modified_stamp.__str__()}, TRANSMITTED: {self.transmit_stamp.__str__()}\nARTICLES: [{self.articles}]"
