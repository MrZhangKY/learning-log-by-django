from django.db import models

# Create your models here.
class Topic(models.Model):
    '''topic of learning of users'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''return string format of model'''
        return self.text


class Entry(models.Model):
    '''knowledge about a specific area'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        '''return string format of model'''
        return self.text[:50] + '...'