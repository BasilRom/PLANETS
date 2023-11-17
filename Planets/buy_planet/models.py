from django.db import models
from django.urls import reverse


class Planet(models.Model):
    name = models.CharField('Название',max_length=15)
    price = models.IntegerField('Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    description = models.TextField('Описание')
    photo = models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')
    bought = models.TextField('Покупка', null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('planet', kwargs={'planet_id': self.pk})

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def get_self_url(self):
        return reverse('buy', kwargs={'planet_id': self.pk})



class Category(models.Model):
    cat = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.cat

    def get_absolute_url(self):
        # return reverse('categs', kwargs={'cat_id': self.pk})
        return reverse('categs', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'