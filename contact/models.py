from django.db import models
from core.models import AbstractModel


# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default='',
        verbose_name='Name',
        max_length=255,
        blank=True,
        help_text='',
    )
    email = models.EmailField(
        default='',
        verbose_name='Email',
        max_length=255,
        blank=True,
        help_text='',
    )
    subject = models.CharField(
        default='',
        verbose_name='Subject',
        max_length=255,
        blank=True,
        help_text='',
    )
    message = models.TextField(
        default='',
        verbose_name='Message',
        blank=True,
        help_text='',
    )

    def __str__(self):
        return f'Message: {self.name}'


    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('name', )


