from django.db import models

# Create your models here.
from django.db import models

class Record(models.Model):
    key1 = models.CharField(max_length=50)
    value1 = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.key1} - {self.value1}'

from django.db import models

class MyData(models.Model):
    key1 = models.CharField(max_length=50)
    value1 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.key1}: {self.value1}"

