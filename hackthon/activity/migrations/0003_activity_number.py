# Generated by Django 2.2 on 2019-04-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20190420_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
