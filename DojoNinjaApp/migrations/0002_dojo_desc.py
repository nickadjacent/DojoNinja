# Generated by Django 2.2 on 2020-02-13 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DojoNinjaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
    ]
