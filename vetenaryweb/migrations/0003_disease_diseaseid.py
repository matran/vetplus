# Generated by Django 4.1.7 on 2023-03-06 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vetenaryweb', '0002_alter_disease_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='diseaseid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
