# Generated by Django 4.1.7 on 2023-03-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetenaryweb', '0003_disease_diseaseid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.DeleteModel(
            name='Symptoms',
        ),
    ]
