# Generated by Django 4.1 on 2022-09-08 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_room_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='type',
            field=models.TextField(null=True),
        ),
    ]