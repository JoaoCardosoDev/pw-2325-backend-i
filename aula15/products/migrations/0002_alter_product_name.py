# Generated by Django 5.0.4 on 2024-04-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
