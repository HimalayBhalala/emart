# Generated by Django 4.2.7 on 2023-12-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0006_auto_20231226_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
