from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name='Başlık Giriniz',
                             help_text='Başlık Bilgisi Burada Girilir.')
    content = models.TextField(max_length=1000, blank=False, null=True, verbose_name='İçerik Giriniz')
    created_date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = 'Gönderiler'
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.title)
