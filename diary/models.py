from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Diary(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    time=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True)
        
    def __str__ (self):
        return self.title +" - "+ self.content

    def summary(self):
        return self.content[:50]
        
class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    diary=models.ForeignKey(Diary, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)