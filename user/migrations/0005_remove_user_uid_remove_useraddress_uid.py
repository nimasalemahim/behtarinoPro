# Generated by Django 4.0.5 on 2022-06-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_useraddress_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='uid',
        ),
    ]
