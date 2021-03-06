# Generated by Django 3.1 on 2021-12-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0037_auto_20211206_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='equip_1',
            field=models.CharField(choices=[('Hat', 'Hat'), ('Gloves', 'Gloves'), ('Shoes', 'Shoes')], default='Hat', max_length=64),
        ),
        migrations.AddField(
            model_name='character',
            name='equip_2',
            field=models.CharField(choices=[('Hairpin', 'Hairpin'), ('Bag', 'Bag'), ('Badges', 'Badges')], default='Hairpin', max_length=64),
        ),
        migrations.AddField(
            model_name='character',
            name='equip_3',
            field=models.CharField(choices=[('Wristwatch', 'Wristwatch'), ('Amulet', 'Amulet'), ('Necklace', 'Necklace')], default='Wristwatch', max_length=64),
        ),
    ]
