# Generated by Django 4.2.6 on 2023-10-27 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
