# Generated by Django 4.2.2 on 2023-09-22 16:20

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('course_name', models.CharField(max_length=256)),
                ('desc', models.CharField(max_length=256)),
                ('video_url', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('video_file', models.FileField(null=True, upload_to='videos/', verbose_name='video')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
