from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from djangoResume.custom_storages import DocumentStorage, ImageSettingStorage


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
        storage=ImageSettingStorage(),
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


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Company Name',
        help_text='This is variable of company name.',
    )
    job_title = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Job Title',
        help_text='This is variable of job title.',
    )
    job_location = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Job Location',
        help_text='This is variable of job location.',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)


class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='School Name',
        help_text='This is variable of school name.',
    )
    major = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )

    def __str__(self):
        return f'Experience: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default='',
        blank=True,
        max_length=255,
        verbose_name='Link',
    )
    icon = models.CharField(
        default='',
        blank=True,
        max_length=255,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'Experience: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)


class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug = models.SlugField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of user name.',
    )
    button_text = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Button Text',
        help_text='This is variable of user name.',
    )
    file = models.FileField(
        default='',
        blank=True,
        verbose_name='File',
        help_text='',
        storage=DocumentStorage()
    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
