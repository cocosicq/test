# Generated by Django 2.2.1 on 2019-05-31 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_remote_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remote_post',
            name='text',
            field=models.DateField(),
        ),
    ]
