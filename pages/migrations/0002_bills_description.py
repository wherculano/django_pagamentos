# Generated by Django 3.2.8 on 2021-10-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='description',
            field=models.CharField(default='Description', max_length=50),
            preserve_default=False,
        ),
    ]