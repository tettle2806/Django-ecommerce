# Generated by Django 4.2.7 on 2024-01-23 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.AlterModelTable(
            name='categories',
            table='category',
        ),
    ]
