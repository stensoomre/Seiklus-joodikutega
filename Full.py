from random import *
from time import *
import os

debug = 1  # Sätti see '1', et muuta allolevaid muutujaid kergesti :)

def main():
    os.system('cls')
    print(f"""
                    =====================
                    Seiklused Joodikutega
                    =====================
                    
                 Salvestamise test - TEST1 (done)
                 Laadmise test     - TEST2
                 New char test     - TEST3 (done)
                 Combat test.      - TEST4
                 Looting test.     - TEST5
          Armory and equiping test - TEST6
                 Tunnustused       - CREDITS (done)
                 
""")
    s = input().upper()
    if s == "TEST1":
        os.system('cls')
        savetest()
    if s == "TEST2":
        os.system('cls')
        loadtest()
    if s == "TEST3":
        os.system("cls")
        newchar()
    if s == "TEST4":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "TEST5":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "TEST":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "CREDITS":
        os.system('cls')
        print(f"""

                    Pea-Arendaja: Sten Soomre
                    Kaas-Arendaja: Erik Teppan
                    
                    
                    
                    Tänud kõikidele inimestele,
                    kes feedbacki antsid :)

    """)
        sleep(5)
        main()

def level_up_check():
    global xp_current # Global on supreme
    global xp_needed # Global on supreme
    global playerlevel # Global on supreme
    if xp_current>xp_needed: # Kui xp on suurem kui xp max
            xp_current -= xp_needed # võta maha
            playerlevel += 1 # level up :)
            if debug == 1:
                print(f"Level up! Leveled to {playerlevel}!!")
            xp_needed = round(xp_needed+(playerlevel*100.275),0)
            level_up_check()
def savetest():
    global playerattack
    global playerdef
    global playerdex
    global playermana
    global playerint
    global playerluck
    global playerspecials
    global playerlevel # Mariole muidugi meeldib ;)
    global relv
    global relv_min
    global relv_max
    global ruu
    global ruu_def
    global aksessuaar
    global aksessuaar_info
    global xp_current
    global xp_needed
    global playerclass
    global playerskoor
    
    if debug == 1:
        nimi = input("Siseta nimi: ")

        playerattack = int(input("Sisesta ATK (int): "))
        playerdef = int(input("Sisesta DEF (int): "))
        playerdex = int(input("Sisesta DEX (int): "))
        playermana = int(input("Sisesta MANA (int): "))
        playerint = int(input("Sisesta INT (int): "))
        playerluck = int(input("Sisesta LUCK (int): "))
        playerspecials = input("Sisesta SPECIALS (string): ")

        relv = input("Sisesta relva nimi (string): ")
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = input("Sisesta relva specid (string): ")
        ruu = input("Sisesta rüü nimi (string): ")
        ruu_def = 0
        playerdef2 = ruu_def + playerdef
        aksessuaar = input("Sisesta aksessuaari nimetus (string): ")
        aksessuaar_info = None
        playerlevel = 1
        if playerlevel == 1:
            xp_needed = 100
            xp_current = 0#round(randint(1,100000),0)
        if xp_current>xp_needed:
            level_up_check()
        playerclass = input("Sisesta class (string): ")
        playerskoor = int(input("Sisesta skoor (int): "))


    f= open(f"SAVE/{nimi}.txt","w+", encoding="UTF-8")
    f.write(f"Nimi: {nimi}\n")
    f.write(f"Level: {playerlevel} ({xp_current}XP/{xp_needed}XP)\n")
    f.write("---------------------\n")
    f.write(f"ATK: {playerattack} ({relv_min}-{relv_max})DMG\n")
    f.write(f"DEF: {playerdef} ({playerdef2})\n")
    f.write(f"DEX: {playerdex}\n")
    f.write(f"MANA: {playermana}\n")
    f.write(f"INT: {playerint}\n")
    f.write(f"LUCK: {playerluck}\n")
    f.write(f"SPECIALS: {playerspecials}\n")
    f.write("---------------------\n")
    f.write(f"RELV: {relv} {relva_info}\n")
    f.write(f"RÜÜ: {ruu} +({ruu_def} DEF)\n")
    f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
    f.write("---------------------\n")
    f.write(f"Klass: {playerclass}\n")
    f.write(f"Skoor: {playerskoor}\n")
    f.close()
    sleep(1)
    print("")
    print(f"Salvestatud {nimi}.txt'ina")
    sleep(4)
    main()
    
    
def newchar():
    global playerattack
    global playerdef
    global playerdef2
    global playerdex
    global playermana
    global playerint
    global playerluck
    global playerspecials
    global playerlevel # Mariole muidugi meeldib ;)
    global relv
    global relv_min
    global relv_max
    global ruu
    global ruu_def
    global aksessuaar
    global aksessuaar_info
    global xp_current
    global xp_needed
    global playerclass
    global playerskoor
    nimi = input("Siseta nimi: ")
    playerattack = 1
    playerdef = 1
    playerdex = 1
    playermana = 1
    playerint = 1
    playerluck = 1
    playerspecials = 1

    relv = "Oks"
    relv_min = 1
    relv_min = relv_min+(playerattack*2.5)
    relv_max = 2
    relv_max = relv_max+(playerattack*2.5)
    relva_info = "\"Vanakoolne puit oks\""
    ruu = "Saapad"
    ruu_def = 2
    playerdef2 = ruu_def + playerdef
    aksessuaar = "Nöör"
    aksessuaar_info = None
    playerlevel = 1
    if playerlevel == 1:
        xp_needed = 100
        xp_current = 0#round(randint(1,100000),0)
    if xp_current>xp_needed:
        level_up_check()
    playerclass = "Maag"
    playerskoor = 0

    f= open(f"SAVE/{nimi}.txt","w+", encoding="UTF-8")
    f.write(f"Nimi: {nimi}\n")
    f.write(f"Level: {playerlevel} ({xp_current}XP/{xp_needed}XP)\n")
    f.write("---------------------\n")
    f.write(f"ATK: {playerattack} ({relv_min}-{relv_max})DMG\n")
    f.write(f"DEF: {playerdef} ({playerdef2})\n")
    f.write(f"DEX: {playerdex}\n")
    f.write(f"MANA: {playermana}\n")
    f.write(f"INT: {playerint}\n")
    f.write(f"LUCK: {playerluck}\n")
    f.write(f"SPECIALS: {playerspecials}\n")
    f.write("---------------------\n")
    f.write(f"RELV: {relv} {relva_info}\n")
    f.write(f"RÜÜ: {ruu} +({ruu_def} DEF)\n")
    f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
    f.write("---------------------\n")
    f.write(f"Klass: {playerclass}\n")
    f.write(f"Skoor: {playerskoor}\n")
    f.close()
    sleep(1)
    print("")
    print(f"Salvestatud {nimi}.txt'ina")
    sleep(4)
    main()
    
def loadtest():
    pass
main()
