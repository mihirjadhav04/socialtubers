# Generated by Django 5.1 on 2024-08-26 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=100, unique=True)),
                ('view_count', models.BigIntegerField()),
                ('subscriber_count', models.BigIntegerField()),
                ('video_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('view_count', models.BigIntegerField()),
                ('like_count', models.BigIntegerField()),
                ('comment_count', models.BigIntegerField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='youtube_apis.youtubechannel')),
            ],
        ),
    ]
