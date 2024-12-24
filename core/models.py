from django.db import models

class TestInsert(models.Model):
    data = models.CharField(max_length = 10)
