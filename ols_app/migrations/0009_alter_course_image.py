# Generated by Django 4.2.2 on 2023-10-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ols_app', '0008_remove_course_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, unique=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
