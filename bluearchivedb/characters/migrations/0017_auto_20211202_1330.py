# Generated by Django 3.1 on 2021-12-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20211202_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Normal_Desc',
            field=models.CharField(default='', max_length=384),
        ),
        migrations.AddField(
            model_name='character',
            name='Normal_Title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='character',
            name='Passive_Desc',
            field=models.CharField(default='', max_length=384),
        ),
        migrations.AddField(
            model_name='character',
            name='Passive_Title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='character',
            name='Sub_Desc',
            field=models.CharField(default='', max_length=384),
        ),
        migrations.AddField(
            model_name='character',
            name='Sub_Title',
            field=models.CharField(default='', max_length=64),
        ),
    ]