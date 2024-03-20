from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=50, verbose_name='название')
    descrition = models.TextField(verbose_name='описпние')
    image = models.ImageField(upload_to='img/post/', verbose_name='фото')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'дата')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self) -> str:
        return f'Название пота {self.title}, Опублековано {self.created.date()}'
