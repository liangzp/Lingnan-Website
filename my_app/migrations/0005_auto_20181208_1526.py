# Generated by Django 2.2 on 2018-12-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20181208_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='endtime',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='application',
            name='fromtime',
            field=models.IntegerField(default=1),
        ),
    ]