from django.db import models
from django.db.models.fields import CharField, IntegerField
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
    ABYDOS,GEHENNA,MILLENNIUM,TRINITY = "Abydos High School","Gehenna Academy", "Millennium Science School","Trinity General School"
    HYAKKIYAKO,SHANHAIJING = "Allied Hyakkiyako Academy","Shanhaijing Senior Secondary School"
    # RED_WINTER,VALKYRIE,ARIUS = "Red Winter","Valkyrie","Arius"
    SCHOOL_CHOICES = (
        (ABYDOS,"Abydos High School"),(GEHENNA,"Gehenna Academy"),(MILLENNIUM,"Millennium Science School"),(TRINITY,"Trinity General School"),
        (HYAKKIYAKO,"Allied Hyakkiyako Academy"),(SHANHAIJING,"Shanhaijing Senior Secondary School")
        # (RED_WINTER,"Red Winter"),(VALKYRIE,"Valkyrie"),(ARIUS,"Arius")
    )
    # CLUB
    




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
    HG,AR,MG,SG,DSG,SMG,SR,MT,GL = "HG","AR","MG","SG","DSG","SMG","SR","MT","GL"
    WEAPON_CHOICES = (
        (HG,"Handgun"),(AR,"Assault Rifle"),(MG,"Machine Gun"),(SG,"Shotgun"),(DSG,"Dual Shotgun"),
        (SMG,"Submachine Gun"),(SR,"Sniper Rifle"),(MT,"Mortar"),(GL,"Grenade Launcher")
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
    
    # Equip 1
    HAT,GLOVES,SHOES ="Hat","Gloves","Shoes"
    EQUIP_1_CHOICES =(
        (HAT,"Hat"),(GLOVES,"Gloves"),(SHOES,"Shoes")
    )

    # Equip 2
    HAIRPIN,BAG,BADGES ="Hairpin","Bag","Badges"
    EQUIP_2_CHOICES =(
        (HAIRPIN,"Hairpin"),(BAG,"Bag"),(BADGES,"Badges")
    )

    # Equip 3
    WRISTWATCH,AMULET,NECKLACE ="Wristwatch","Amulet","Necklace"
    EQUIP_3_CHOICES =(
        (WRISTWATCH,"Wristwatch"),(AMULET,"Amulet"),(NECKLACE,"Necklace")
    )

    # Basic Info
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
    equip_1 = models.CharField(max_length=64,default=HAT,choices=EQUIP_1_CHOICES)
    equip_2 = models.CharField(max_length=64,default=HAIRPIN,choices=EQUIP_2_CHOICES)
    equip_3 = models.CharField(max_length=64,default=WRISTWATCH,choices=EQUIP_3_CHOICES)


    def __str__(self):
        return f"{self.name} {self.rarity}"