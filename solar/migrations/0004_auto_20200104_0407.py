# Generated by Django 2.1.1 on 2020-01-04 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0003_post_link_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]