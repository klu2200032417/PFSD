# Generated by Django 5.0.2 on 2024-03-09 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0007_channel'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('search_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=100000000)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='search',
            field=models.CharField(default=datetime.datetime(2024, 3, 9, 20, 8, 59, 566657, tzinfo=datetime.timezone.utc), max_length=2000),
            preserve_default=False,
        ),
    ]
