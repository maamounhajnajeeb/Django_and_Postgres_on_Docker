from django.db import models

# Create your models here.

class Names(models.Model):
    name = models.CharField(max_length=32, null=False)
    
    def __str__(self) -> str:
        return f"{self.name}"
