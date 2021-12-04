# Generated by Django 3.1 on 2021-12-03 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0027_remove_character_portrait_filepath'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='Armor',
            new_name='armor',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Basic_Desc',
            new_name='basic_desc',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Basic_Title',
            new_name='basic_title',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Damage',
            new_name='damage',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='EX_Cost',
            new_name='ex_cost',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='EX_Desc',
            new_name='ex_desc',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='EX_Title',
            new_name='ex_title',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Position',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Rarity',
            new_name='rarity',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='School',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Sub_Desc',
            new_name='sub_desc',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Sub_Title',
            new_name='sub_title',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='Weapon',
            new_name='weapon',
        ),
    ]