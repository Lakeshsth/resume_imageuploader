# Generated by Django 4.1.7 on 2023-04-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_alter_resume_uploader_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_uploader',
            name='my_file',
            field=models.FileField(blank=True, upload_to='document'),
        ),
    ]