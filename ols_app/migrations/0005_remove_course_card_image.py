# Generated by Django 4.2.2 on 2023-10-03 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ols_app', '0004_alter_course_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='card_image',
        ),
    ]