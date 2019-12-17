from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    t_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,unique=True)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class access_details(models.Model):
    webpage_name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    accessdate=models.DateField()

    def __str__(self):
        return str(self.accessdate) 
    
    
    
