# Generated by Django 2.2.4 on 2023-12-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_ninjas_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjas',
            name='desc',
        ),
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='old_dojo'),
            preserve_default=False,
        ),
    ]
