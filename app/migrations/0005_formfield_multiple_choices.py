# Generated by Django 3.0.6 on 2020-05-30 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200530_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='multiple_choices',
            field=models.TextField(blank=True, help_text="The choices for a multiple choice field. Include one option per line. This field will be ignored for fields that aren't Multiple Choice ones.", max_length=1024, verbose_name='Multiple Choice Choices'),
        ),
    ]
