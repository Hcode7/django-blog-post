# Generated by Django 5.0.7 on 2024-07-15 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 17, 52, 30, 492904, tzinfo=datetime.timezone.utc)),
        ),
    ]
