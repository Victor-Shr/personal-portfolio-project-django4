# Generated by Django 4.0 on 2021-12-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AlterField(
            model_name='project',
            name='data',
            field=models.DateField(),
        ),
    ]