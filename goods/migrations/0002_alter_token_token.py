# Generated by Django 4.2.10 on 2024-02-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.UUIDField(unique=True),
        ),
    ]
