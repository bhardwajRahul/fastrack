# Generated by Django 3.0.8 on 2020-09-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0007_auto_20200819_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageviewmodel',
            name='referrer',
            field=models.CharField(max_length=255),
        ),
    ]
