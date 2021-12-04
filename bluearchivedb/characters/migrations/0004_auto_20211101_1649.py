# Generated by Django 3.1 on 2021-11-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20211101_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='armor',
            field=models.CharField(choices=[('Light Armor', 'Light Armor'), ('Heavy Armor', 'Heavy Armor'), ('Special Armor', 'Special Armor')], max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='damage',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Explosion', 'Explosion'), ('Penetration', 'Penetration'), ('Mystic', 'Mystic')], max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='position',
            field=models.CharField(choices=[('Front', 'Front'), ('Middle', 'Middle'), ('Back', 'Back')], max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='school',
            field=models.CharField(choices=[('Abydos', 'Abydos'), ('Gehenna', 'Gehenna'), ('Millennium', 'Millennium'), ('Trinity', 'Trinity'), ('Hyakkiyako', 'Hyakkiyako'), ('Shanhaijing', 'Shanhaijing'), ('Red Winter', 'Red Winter'), ('Valkyrie', 'Valkyrie'), ('Arius', 'Arius')], max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon',
            field=models.CharField(choices=[('HG', 'HG'), ('AR', 'AR'), ('MG', 'MG'), ('SG', 'SG'), ('SMG', 'SMG'), ('SR', 'SR'), ('RF', 'RF'), ('GL', 'GL')], max_length=3),
        ),
    ]