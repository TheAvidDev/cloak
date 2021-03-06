# Generated by Django 3.0.6 on 2020-05-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200530_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True, help_text='A description for this form that describes its purpose.', max_length=1024, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='description',
            field=models.TextField(help_text='A description that will be shown under the question in smaller text.', max_length=1024, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='formfieldresponse',
            name='content',
            field=models.TextField(help_text='A JSON data object for storing response data.', max_length=8191, verbose_name='Content'),
        ),
    ]
