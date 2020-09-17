# Generated by Django 3.1.1 on 2020-09-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menocare', '0004_auto_20200914_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='MenoCare', max_length=200, null=True, unique=True),
        ),
    ]
