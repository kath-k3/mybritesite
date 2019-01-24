from django.db import models

from django.utils.six import python_2_unicode_compatible
from django.urls import reverse


@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProductArea(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    client_priority = models.PositiveIntegerField(db_index=True, null=True, blank=True)
    product_area = models.ForeignKey(ProductArea, on_delete=models.PROTECT)
    ordered_field_name = 'client_priority'
    ordered_to = 'client'


    class Meta:
        ordering = ('client', 'client_priority')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('featurereq:index')

