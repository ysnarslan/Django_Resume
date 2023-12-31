# Generated by Django 4.2.6 on 2023-10-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('school_name', models.CharField(blank=True, default='', help_text='This is variable of school name.', max_length=255, verbose_name='School Name')),
                ('major', models.CharField(blank=True, default='', max_length=255, verbose_name='Major')),
                ('department', models.CharField(blank=True, default='', max_length=255, verbose_name='Department')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ('start_date',),
            },
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('-start_date',), 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
    ]
