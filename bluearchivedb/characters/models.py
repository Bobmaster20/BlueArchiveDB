from django.db import models
from django.db.models.fields import IntegerField
from django.conf import settings
import os

def imagess_path():
    return os.path.join(settings.STATIC_URL,'characters/img')

# Create your models here.
class Character(models.Model):
    # RARITY
    ONE_STAR,TWO_STAR,THREE_STAR = "*","**","***"
    RARITY_CHOICES = (
        (ONE_STAR,"1 Star"),(TWO_STAR,"2 Star"),(THREE_STAR,"3 Star")
    )
    # SCHOOL
    ABYDOS,GEHENNA,MILLENNIUM,TRINITY = "Abydos","Gehenna", "Millennium","Trinity"
    HYAKKIYAKO,SHANHAIJING,RED_WINTER,VALKYRIE = "Hyakkiyako","Shanhaijing", "Red Winter","Valkyrie"
    ARIUS = "Arius"
    SCHOOL_CHOICES = (
        (ABYDOS,"Abydos"),(GEHENNA,"Gehenna"),(MILLENNIUM,"Millennium"),(TRINITY,"Trinity"),
        (HYAKKIYAKO,"Hyakkiyako"),(SHANHAIJING,"Shanhaijing"),(RED_WINTER,"Red Winter"),(VALKYRIE,"Valkyrie"),
        (ARIUS,"Arius")
    )
    # ROLE
    ATTACKER,SUPPORT,TANK,HEALER,TACTICAL = "Attacker","Support","Tank","Healer","Tactical"
    ROLE_CHOICES = (
        (ATTACKER,"Attacker"),
        (SUPPORT,"Support"),
        (TANK,"Tank"),
        (HEALER,"Healer"),
        (TACTICAL,"Tactical")
    )
    # POSITION
    FRONT,MIDDLE,BACK = "Front","Middle","Back"
    POSITION_CHOICES = (
        (FRONT,"Front"),
        (MIDDLE,"Middle"),
        (BACK,"Back"),
    )
    # WEAPON
    HG,AR,MG,SG,SMG,SR,RF,GL = "HG","AR","MG","SG","SMG","SR","RF","GL"
    WEAPON_CHOICES = (
        (HG,"HG"),(AR,"AR"),(MG,"MG"),(SG,"SG"),(SMG,"SMG"),(SR,"SR"),(RF,"RF"),(GL,"GL")
    )
    # DAMAGE
    NORMAL,EXPLOSIVE,PIERCING,MYSTIC = "Normal","Explosive","Piercing","Mystic"
    DAMAGE_CHOICES = (
        (NORMAL,"Normal"),
        (EXPLOSIVE,"Explosive"),
        (PIERCING,"Piercing"),
        (MYSTIC,"Mystic")
    )
    # ARMOR
    LIGHT,HEAVY,SPECIAL = "Light","Heavy","Special"
    ARMOR_CHOICES = (
        (LIGHT,"Light"),(HEAVY,"Heavy"),(SPECIAL,"Special")
    )
    # EX COST
    ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN = 1,2,3,4,5,6,7,8,9,10
    EX_COST_CHOICES = (
        (ONE,"1"),(TWO,"2"),(THREE,"3"),(FOUR,"4"),(FIVE,"5"),(SIX,"6"),(SEVEN,"7"),(EIGHT,"8"),(NINE,"9"),(TEN,"10")
    )

    # SKILL TYPE
    # OFFENSIVE_BUFF,DEFENSIVE_BUFF,OFFENSIVE_DEBUFF,DEFENSIVE_DEBUFF = "OFFENSIVE_BUFF"
    # SINGLE_DMG,AOE_DMG,FAN_DMG,LINE_DMG,SCALING_DMG = ""
    # HEAL,REGEN,BARRIER = ""



    name = models.CharField(max_length=64)
    desc_head = models.CharField(max_length=128,default="")
    desc_body = models.TextField(max_length=384,default="")
    rarity = models.CharField(max_length=3,default=ONE_STAR,choices=RARITY_CHOICES)
    school = models.CharField(max_length=64,default=ABYDOS,choices=SCHOOL_CHOICES)
    role = models.CharField(max_length=64,default=ATTACKER,choices=ROLE_CHOICES)
    position = models.CharField(max_length=64,default=FRONT,choices=POSITION_CHOICES)
    weapon = models.CharField(max_length=3,default=HG,choices=WEAPON_CHOICES)
    damage = models.CharField(max_length=64,default=NORMAL,choices=DAMAGE_CHOICES)
    armor = models.CharField(max_length=64,default=LIGHT,choices=ARMOR_CHOICES)
    ex_title = models.CharField(max_length=64,default="")
    ex_cost = models.IntegerField(default=ONE,choices=EX_COST_CHOICES)
    ex_desc = models.TextField(max_length=384,default="")
    basic_title = models.CharField(max_length = 64,default="")
    basic_desc = models.TextField(max_length = 384,default="")
    enhanced_title = models.CharField(max_length = 64,default="")
    enhanced_desc = models.TextField(max_length = 384,default="")
    sub_title = models.CharField(max_length = 64,default="")
    sub_desc = models.TextField(max_length = 384,default="")
    # hp = models.IntegerField()
    # attack = models.IntegerField()
    # defense = models.IntegerField()
    # healing = models.IntegerField()
    # equip_1 = models.CharField(max_length=64)
    # equip_2 = models.CharField(max_length=64)
    # equip_3 = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.name} {self.rarity}"