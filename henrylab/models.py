from __future__ import unicode_literals
from django import forms
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish = True)
    
class Blog(models.Model):
    author = models.ForeignKey('auth.user', null=True)
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField(max_length =200, unique = True)
    publish = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    objects = EntryQuerySet.as_manager()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
        
class Profile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "profile"
