# Generated by Django 3.0.8 on 2020-08-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0006_pageviewmodel_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageviewmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]