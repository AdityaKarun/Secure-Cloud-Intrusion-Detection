# Generated by Django 5.0.7 on 2024-07-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0006_alter_cloudlog_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudlog',
            name='file_path',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
