# Generated by Django 2.2.4 on 2022-09-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220918_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvariation',
            name='attachment',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]