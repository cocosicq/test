# Generated by Django 2.2.1 on 2019-05-31 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_remote_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='remote_post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
