# Generated by Django 2.2.1 on 2019-06-04 21:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 21, 4, 1, 550712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='participant',
            name='is_captain',
            field=models.BooleanField(default=False, verbose_name='Captain'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
