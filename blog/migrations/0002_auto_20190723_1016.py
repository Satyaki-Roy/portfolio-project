# Generated by Django 2.2.1 on 2019-07-23 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='images',
            new_name='image',
        ),
    ]
