# Generated by Django 4.2.6 on 2023-10-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Icon'),
        ),
    ]
