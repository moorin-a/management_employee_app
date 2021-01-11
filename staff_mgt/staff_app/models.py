from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    gender = models.IntegerField()
    
    def __str__(self):
        return 'id: %s, 名前: %s, email: %s, gender: %s' %(str(self.id), str(self.name), str(self.email), str(self.gender))