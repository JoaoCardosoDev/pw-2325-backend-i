# Generated by Django 5.0.4 on 2024-04-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='The name of the product', max_length=100),
        ),
    ]
