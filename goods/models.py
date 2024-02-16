from django.db import models


class Token(models.Model):

    token = models.UUIDField(max_length=37, unique=True)

    def create_token(self, new_token):
        self.token = new_token
        self.save()


class Good(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField()
    price = models.IntegerField()
