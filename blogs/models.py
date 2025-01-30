from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from root.models import Reporter



        
class Category(models.Model):
    name = models.CharField(max_length= 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Blogs(models.Model):
    name = models.CharField(max_length= 100)
    reporters = models.ForeignKey(Reporter,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    fee = models.FloatField(default= 100)
    likes = models.IntegerField()
    capacity = models.IntegerField(default= 20)
    image = models.ImageField(upload_to='new',default='news.jpg')
    schedule = models.DateTimeField(default= timezone.now)
    content = models.TextField(default='good news')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Comment(models.Model):
    course = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
