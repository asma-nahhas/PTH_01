# Generated by Django 3.1.3 on 2020-11-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0002_table_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='fileIndex',
            field=models.IntegerField(null=True),
        ),
    ]
