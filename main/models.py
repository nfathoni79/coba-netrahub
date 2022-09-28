from django.db import models

# Create your models here.


class InboxMessage(models.Model):
    payload = models.CharField(max_length=200)
    data_type = models.CharField(max_length=10, default='TEXT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class OutboxMessage(models.Model):
    payload = models.CharField(max_length=200)
    data_type = models.CharField(max_length=10, default='TEXT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    ongoing = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
