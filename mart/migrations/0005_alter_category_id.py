# Generated by Django 4.2.7 on 2023-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0004_auto_20231224_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
