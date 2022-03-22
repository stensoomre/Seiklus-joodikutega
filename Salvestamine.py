from time import *
from random import *
import re

nimi = input("Siseta nimi: ")

playerattack = int(input("Sisesta ATK (int): "))
playerdef = int(input("Sisesta DEF (int): "))
playerdex = int(input("Sisesta DEX (int): "))
playermana = int(input("Sisesta MANA (int): "))
playerint = int(input("Sisesta INT (int): "))
playerluck = int(input("Sisesta LUCK (int): "))
playerspecials = input("Sisesta SPECIALS (string): ")

relv = input("Sisesta relva nimi (string): ")
relv_min = randint(1,30)
relv_max = randint(30,50)
ruu = input("Sisesta rüü nimi (string): ")
ruu_def = randint(1,300)
playerdef += ruu_def
aksessuaar = input("Sisesta aksessuaari nimetus (string): ")
aksessuaar_info = "\"Mdea sa oled pede\""


f= open(f"{nimi}.txt","w+", encoding="UTF-8")
f.write(f"Nimi: {nimi}\n")
f.write("---------------------\n")
f.write(f"ATK: {playerattack}\n")
f.write(f"DEF: {playerdef}\n")
f.write(f"DEX: {playerdex}\n")
f.write(f"MANA: {playermana}\n")
f.write(f"INT: {playerint}\n")
f.write(f"LUCK: {playerluck}\n")
f.write(f"SPECIALS: {playerspecials}\n")
f.write("---------------------\n")
f.write(f"RELV: {relv} ({relv_min}-{relv_max})\n")
f.write(f"RÜÜ: {ruu} +{ruu_def} DEF\n")
f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
f.close()
