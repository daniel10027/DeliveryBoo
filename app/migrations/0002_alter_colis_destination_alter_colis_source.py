# Generated by Django 5.0.1 on 2024-01-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colis',
            name='destination',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='colis',
            name='source',
            field=models.TextField(),
        ),
    ]