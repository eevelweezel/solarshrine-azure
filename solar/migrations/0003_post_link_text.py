# Generated by Django 2.1.1 on 2019-12-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0002_auto_20191218_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_text',
            field=models.CharField(default='title text', max_length=256),
            preserve_default=False,
        ),
    ]
