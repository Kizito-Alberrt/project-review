# Generated by Django 3.1.7 on 2021-04-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_category_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
