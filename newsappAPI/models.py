from django.db import models

# Create your models here.
    

class Item(models.Model):
    item_id = models.IntegerField(unique=True, blank=False)
    deleted = models.BooleanField(default=False)
    # type = models.ForeignKey(Type, related_name='types', on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=128, blank=True)
    by = models.CharField(max_length=255, blank=True)
    time = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    dead = models.BooleanField(default=False)
    parent = models.IntegerField(blank=True, null=True)
    kids =  models.JSONField('kids', default=dict)
    url = models.URLField(max_length=255, blank=True)
    score = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    descendants = models.IntegerField(blank=True, default=0, null=True)
    poll = models.IntegerField(blank=True, null=True)
    parts = models.JSONField('parts', default=dict)
    source = models.CharField(max_length=255, default='HN')







    
