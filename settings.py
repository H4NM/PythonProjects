import pygame as pg
vec = pg.math.Vector2

#THE COLORS (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 200, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)


#MAP DETAILS
LIST_OF_MAPS = ['level1.tmx', 'samplemap.tmx']
WIDTH = 900
HEIGHT = 700
FPS = 60
TITLE = "Game of the year edition"
MELEE_DISTANCE = 10

#LAYERS
WALL_LAYER = 1
CAR_LAYER = 4
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

#ITEMS SETTINGS
BOB_RANGE = 12
BOB_SPEED = 0.3
ITEM_HIT_RECT = pg.Rect(0, 0, 35, 35)


ITEM_IMAGES = {'basic_sword_1': 'basic_sword_1.png',
               'basic_bow_1': 'basic_bow_1.png'
               }


#PLAYER SETTINGS
PLAYER_HEALTH = 100
PLAYER_SPEED = 220
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 65)
PLAYER_WEAPON_INVENTORY = ['fists']
PLAYER_OTHER_INVENTORY = []

PLAYER_IMG = 'standing.png'

PLAYER_RIGHT_1 = 'R1.png'
PLAYER_RIGHT_2 = 'R2.png'
PLAYER_RIGHT_3 = 'R3.png'
PLAYER_RIGHT_4 = 'R4.png'
PLAYER_RIGHT_5 = 'R5.png'
PLAYER_RIGHT_6 = 'R6.png'
PLAYER_RIGHT_7 = 'R7.png'
PLAYER_RIGHT_8 = 'R8.png'
PLAYER_RIGHT_9 = 'R9.png'

PLAYER_LEFT_1 = 'L1.png'
PLAYER_LEFT_2 = 'L2.png'
PLAYER_LEFT_3 = 'L3.png'
PLAYER_LEFT_4 = 'L4.png'
PLAYER_LEFT_5 = 'L5.png'
PLAYER_LEFT_6 = 'L6.png'
PLAYER_LEFT_7 = 'L7.png'
PLAYER_LEFT_8 = 'L8.png'
PLAYER_LEFT_9 = 'L9.png'

#STANDARD ORC MOB SETTINGS
ORC_MOB_HEALTH = 10
ORC_MOB_DAMAGE = 5
ORC_MOB_SPEED = 40
ORC_MOB_DETEC_RADIUS = 140
ORC_MOB_HIT_RECT = pg.Rect(0, 0, 20, 35)
ORC_MOB_IMG = 'L7E.png'

ORC_MOB_RIGHT_1 = 'R1E.png'
ORC_MOB_RIGHT_2 = 'R2E.png'
ORC_MOB_RIGHT_3 = 'R3E.png'
ORC_MOB_RIGHT_4 = 'R4E.png'
ORC_MOB_RIGHT_5 = 'R5E.png'
ORC_MOB_RIGHT_6 = 'R6E.png'
ORC_MOB_RIGHT_7 = 'R7E.png'
ORC_MOB_RIGHT_8 = 'R8E.png'

ORC_MOB_LEFT_1 = 'L1E.png'
ORC_MOB_LEFT_2 = 'L2E.png'
ORC_MOB_LEFT_3 = 'L3E.png'
ORC_MOB_LEFT_4 = 'L4E.png'
ORC_MOB_LEFT_5 = 'L5E.png'
ORC_MOB_LEFT_6 = 'L6E.png'
ORC_MOB_LEFT_7 = 'L7E.png'
ORC_MOB_LEFT_8 = 'L8E.png'



#WEAPON RECT SIZES
LARGE_RECT = pg.Rect(0,0,50,50)
MEDIUM_RECT = pg.Rect(0,0,40,40)
SMALL_RECT = pg.Rect(0,0,30,30)


#WEAPONS AND ITEMS
EMPTY_PIC = 'empty_pic.png'

BASIC_SLASH_ATTACK_1 = 'slash_effect_1.png'
BASIC_SLASH_ATTACK_2 = 'slash_effect_2.png'
BASIC_SLASH_ATTACK_3 = 'slash_effect_3.png'
MELEE_DEMO_ATTACK_IMG = 'melee_demoattack.png'
BASIC_ARROW_1 = 'basic_arrow_1.png'
BASIC_ARROW_2 = 'basic_arrow_2.png'
BASIC_ARROW_3 = 'basic_arrow_3.png'
BASIC_ARROW_4 = 'basic_arrow_4.png'
BASIC_ARROW_5 = 'basic_arrow_5.png'

WEAPONS = {}

#MELEE WEAPONS SETTINGS
WEAPONS['fists'] = {
                         'type': 'melee',
                         'attack_effect': 'strike',
                         'rate': 420,
                         'kickback': 100,
                         'damage': 1,
                         'range': 35,
                         'lifetime': 350,
                         'rect': SMALL_RECT
                         }

WEAPONS['basic_sword_1'] = {
                         'type': 'melee',
                         'attack_effect': 'slash',
                         'rate': 420,
                         'kickback': 200,
                         'damage': 1,
                         'range': 20,
                         'lifetime': 500,
                         'rect': MEDIUM_RECT
                         }

#RANGED WEAPONS SETTINGS
WEAPONS['basic_bow_1'] = {
                         'type': 'ranged',
                         'attack_effect': 'arrow',
                         'rate': 520,
                         'kickback': 200,
                         'damage': 1,
                         'range': 20,
                         'lifetime': 2500,
                         'rect': MEDIUM_RECT,
                         'spread': 3,
                         'speed': 4
                         }
