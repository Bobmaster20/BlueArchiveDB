# Generated by Django 3.1 on 2021-12-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20211202_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='ex_desc',
            field=models.CharField(default='', max_length=192),
        ),
        migrations.AddField(
            model_name='character',
            name='ex_title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
