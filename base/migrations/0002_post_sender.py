# Generated by Django 4.1 on 2022-09-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sender',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
