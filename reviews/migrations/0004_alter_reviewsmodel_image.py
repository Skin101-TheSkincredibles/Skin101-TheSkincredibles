# Generated by Django 4.1 on 2022-12-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_reviewsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
