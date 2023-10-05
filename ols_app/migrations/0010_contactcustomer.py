# Generated by Django 4.2.2 on 2023-10-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ols_app', '0009_alter_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('username', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=256)),
                ('useremail', models.CharField(max_length=256)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]