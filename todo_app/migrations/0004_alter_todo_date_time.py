# Generated by Django 3.2.4 on 2021-09-23 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
