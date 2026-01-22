from django.db import models


class Guide(models.Model):
    trackingNumber = models.CharField(max_length=15, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    currentStatus = models.CharField(max_length=20)



class StatusHistory(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name="statusHistory")
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    updatedBy = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

