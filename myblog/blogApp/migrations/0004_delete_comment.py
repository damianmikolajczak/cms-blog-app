# Generated by Django 3.1.5 on 2021-01-17 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_auto_20210117_0312'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]