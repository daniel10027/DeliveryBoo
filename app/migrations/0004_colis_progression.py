# Generated by Django 5.0.1 on 2024-01-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_colis_description_alter_colis_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colis',
            name='progression',
            field=models.IntegerField(default=0),
        ),
    ]
