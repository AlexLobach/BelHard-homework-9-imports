import enum
import random
import click

@click.command
@click.option ("--choice", prompt = "Want a special toy? (yes/no)", help = "yes/no")

def choice_toy(choice):
        if choice == "no":
            click.echo (f'{random.choice(list(Collor)).name} {random.choice(list(toys)).value} ')
        elif choice == "yes":
            click.echo (f'{random.choice(list(Toy)).value}')

class toys(enum.Enum):
    toy_1 = "ball"
    toy_2 = "angel"
    toy_3 = "animal"
    toy_4 = "fruit"


class Collor(enum.Enum):
    Red = 0xff0000
    Green = 0x00ff00
    Blue = 0x0000ff
    Yelolow = 0xffff00
    Orange = 0XFF8000


class Toy(enum.Enum):
    TOY_1 = "CHRISTMAS TREE"
    TOY_2 = "TREE SKIRT"
    TOY_3 = "ORNAMENTS"
    TOY_4 = "TREE TOPPER"
    TOY_5 = "CHRISTMAS WREATH"
    TOY_6 = "STOCKINGS (AND STOCKING HOOKS)"
    TOY_7 = "SANTA CLAUS FIGURE"
    TOY_8 = "REINDEER"
    TOY_9 = "MINI TREE"
    TOY_10 = "NATIVITY SCENE"
    TOY_11 = "GARLAND"
    TOY_12 = "PUTZ HOUSES"
    TOY_13 = "POINSETTIAS" 
    TOY_14 = "CANDLES"
    TOY_15 = "NATURE"
    TOY_16 = "MISTLETOE"
    TOY_17 = "TINSEL"
    TOY_18 = "NUTCRACKER"
    TOY_19 = "ADVENT CALENDAR"
    TOY_20 = "CHRISTMAS LINENS (BEDDING, SHEETS)"
    TOY_21 = "CHRISTMAS TABLEWARE (PLATES, NAPKINS, SERVING PLATTERS)"
    TOY_22 = "RED VELVET RIBBON BOWS"
    TOY_23 = "FAKE SNOW"
    TOY_24 = "CHRISTMAS CENTERPIECE"
    TOY_25 = "STRING LIGHTS"
   

if __name__ == '__main__':
    choice_toy()
    
    
