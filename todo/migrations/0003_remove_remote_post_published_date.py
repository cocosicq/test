# Generated by Django 2.2.1 on 2019-05-31 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190531_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remote_post',
            name='published_date',
        ),
    ]
