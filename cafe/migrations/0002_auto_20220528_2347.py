# Generated by Django 3.2 on 2022-05-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='power',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='wifi',
            field=models.CharField(max_length=10),
        ),
    ]
