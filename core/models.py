from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
    )

    class Meta:
        abstract = True


# Create your models here.
class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of user name.',
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameter = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of user name.',
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        blank=True,
        verbose_name='Image',
        help_text='',
        upload_to='images/',
    )

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of user name.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)
