# Generated by Django 2.1.1 on 2020-01-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0006_auto_20200104_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
