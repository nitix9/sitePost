from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=60)
    description=models.CharField(max_length=100000)
    image=models.ImageField(upload_to='post_image',blank=True,null=True)
    short_description=models.CharField(max_length=128)
    date=models.DateField()
    
    def __str__(self):
        return f"{self.id}:{self.title}"
    
class Comment(models.Model):
    name=models.CharField(max_length=32)
    text=models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"{self.id}: {self.text}"
