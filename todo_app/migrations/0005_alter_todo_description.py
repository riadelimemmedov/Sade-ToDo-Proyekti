# Generated by Django 3.2.4 on 2021-09-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_todo_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Text'),
        ),
    ]
