# Generated by Django 4.2.2 on 2023-09-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ols_app', '0006_alter_enroll_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='has_finished',
        ),
    ]