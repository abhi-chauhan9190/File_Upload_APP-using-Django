# Generated by Django 4.2.3 on 2023-09-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='Upload_File',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='Upload_Image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]