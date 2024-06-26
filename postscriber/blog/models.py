from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    
    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return self.title
