# Generated by Django 4.1.7 on 2023-03-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='User',
        ),
    ]