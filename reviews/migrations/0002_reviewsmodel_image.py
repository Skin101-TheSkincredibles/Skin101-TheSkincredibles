# Generated by Django 4.1 on 2022-12-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsmodel',
            name='image',
            field=models.ImageField(default='reviews/templates/download.jpg', upload_to='images'),
        ),
    ]
