from os import listdir, makedirs, path
from django.db import models

from .ulib import add_update_row, create_or_add_date_folder_file, get_data_obj




class Footwear(models.Model):
    number = models.CharField(max_length=500, null=False, unique=True)
    type_p = models.ForeignKey('Type', models.PROTECT, null=True, blank=True)
    brand = models.ForeignKey('Brand', models.PROTECT, null=True, blank=True)

    marked = models.ForeignKey('Marked', models.PROTECT, null=True, blank=True)

    color = models.CharField(max_length=500, null=True, blank=True)
    notice = models.CharField(max_length=500, null=True, blank=True)
    country = models.ForeignKey('Country', models.PROTECT, null=True, blank=True)
    size = models.ForeignKey('Size', models.PROTECT, null=True, blank=True)
    sm = models.ForeignKey('Sm', models.PROTECT, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    status = models.ForeignKey('Status', models.PROTECT, null=True, blank=True)
    state = models.ForeignKey('State', models.PROTECT, null=True, blank=True)
    extra_notice = models.CharField(max_length=500, null=True, blank=True)

    date = models.ForeignKey('Date', models.PROTECT, null=False)

    def save(self, *args, **kwargs):
        data = get_data_obj(
            number= self.number,
            type_p= self.type_p,
            brand= self.brand,

            marked= self.marked,

            color= self.color,
            notice= self.notice,
            country= self.country,
            size= self.size,
            sm= self.sm,
            price= self.price,
            old_price= self.old_price,

            status= self.status,
            state= self.state,
            extra_notice= self.extra_notice,

            date=self.date
        )
        super().save(*args, **kwargs)



        #!comment before inizialization and uncommented after
        add_update_row(data)
        #!comment before inizialization and uncommented after


    class Meta:
        verbose_name_plural = "взуття"
        # verbose_name_plural = 'взуття'
        ordering = ['-id']


    def __str__(self):
        return self.number



class Type(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "тип"
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "бренд"
        ordering = ['name']


    def __str__(self):
        return self.name


class Marked(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "маркування"
        ordering = ['name']


    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "країна"
        ordering = ['name']


    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "розмір"
        ordering = ['-size']


    def __str__(self):
        return self.size


class Sm(models.Model):
    sm = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "см"
        ordering = ['-sm']


    def __str__(self):
        return self.sm


class Status(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Статус"
        ordering = ['name']


    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Оцінка товару"
        ordering = ['name']


    def __str__(self):
        return self.name




#! save save >> DONE 
class Date(models.Model):
    date = models.CharField(max_length=500, null=False, unique=True)
    # c = Footwear.objects.annotate(count=Count('date'))
    class Meta:
        verbose_name_plural = "дата"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



        #!comment before inizialization and uncommented after
        create_or_add_date_folder_file(self.date)
        #!comment before inizialization and uncommented after


    def __str__(self):
        return self.date
