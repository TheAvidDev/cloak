# Generated by Django 3.0.6 on 2020-05-30 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of this form.', max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, help_text='A description for this form that describes its purpose.', max_length=1024, verbose_name='Description')),
                ('is_open', models.BooleanField(default=True, help_text='Whether this form is accepting responses.', verbose_name='Open')),
                ('close_datetime', models.DateTimeField(help_text='Optional date and time on which the form will automatically stop accepting responses. Leave blank to disable.', null=True, verbose_name='Auto-Close Date')),
                ('is_public', models.BooleanField(default=False, help_text='Whether this form is displayed on the front page of this site. Great for advertising your form!', verbose_name='Publicly Displayed')),
                ('login_required', models.BooleanField(default=False, help_text='Whether a user is required to make an account to fill out this form.', verbose_name='Requires login')),
                ('is_single_response', models.BooleanField(default=True, help_text="Whether users are only allowed to submit one response. Only works when 'Requires Login' is also enabled.", verbose_name='Single Response')),
                ('form_id', models.CharField(editable=False, help_text='Securely randomly generated base 64 encoded bytes used for form url.', max_length=128, verbose_name='Random Form ID')),
                ('editors', models.ManyToManyField(blank=True, help_text='Users that will be able to edit this form.', related_name='edited_forms', to=settings.AUTH_USER_MODEL, verbose_name='Editors')),
                ('reviewers', models.ManyToManyField(blank=True, help_text='Users that will be able to seee this forms responses.', related_name='reviewed_forms', to=settings.AUTH_USER_MODEL, verbose_name='Reviewers')),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_type', models.CharField(choices=[('M', 'Multiple Choice'), ('N', 'Numeric'), ('S', 'Short Answer'), ('L', 'Long Answer')], default='S', help_text='Type of input.', max_length=1, verbose_name='Input Type')),
                ('is_required', models.BooleanField(default=True, help_text='Whether this field is required to be filled in.', verbose_name='Required')),
                ('is_secret', models.BooleanField(default=False, help_text='Whether this field will be completely hidden from reviewers until the application is accepted.', verbose_name='Secret')),
                ('question', models.CharField(help_text='Question displayed to the user.', max_length=255, verbose_name='Question')),
                ('description', models.CharField(help_text='A description that will be shown under the question in smaller text.', max_length=1024, verbose_name='Description')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app.Form', verbose_name='Form')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of submitter.', max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(help_text='Email address to use for contact.', max_length=254, verbose_name='Email')),
                ('submission_datetime', models.DateTimeField(auto_now_add=True, help_text='Date and time of this response.', verbose_name='Submission Date')),
                ('status', models.CharField(default='P', help_text='Status of this response. Mark as accepted to view secrets and send submitter an acceptance email. Once marked as accepted, the status cannot be changed.', max_length=1, verbose_name='Status')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='app.Form', verbose_name='Form')),
                ('user', models.ForeignKey(help_text='The user who submitted this response. null if no account was used.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='FormFieldResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='A JSON data object for storing response data.', max_length=8191, verbose_name='Content')),
                ('form_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='app.FormField', verbose_name='Form Field')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app.Response', verbose_name='Response')),
            ],
        ),
    ]
