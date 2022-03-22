from random import *
from time import *
debug = 1  # Sätti see '1', et muuta allolevaid muutujaid kergesti :)

def main():
    print(f"""
                    =====================
                    Seiklused Joodikutega
                    =====================
                    
                 Salvestamise test - TEST1
                 Laadmise test     - TEST2
                 Tunnustused       - CREDITS
                 
""")
    s = input()
    if s == "TEST1":
        save()
    if s == "TEST2":
        print("pole midagi veel ):")
        sleep(2)
        main()
    if s == "CREDITS":
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
def save():
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
        relv_min = randint(1,30)
        relv_max = randint(30,50)
        ruu = input("Sisesta rüü nimi (string): ")
        ruu_def = randint(1,300)
        playerdef += ruu_def
        aksessuaar = input("Sisesta aksessuaari nimetus (string): ")
        aksessuaar_info = "\"Mdea sa oled pede\""
        playerlevel = 1
        if playerlevel == 1:
            xp_needed = 100
            xp_current = 100000000#round(randint(1,100000),0)
        if xp_current>xp_needed:
            level_up_check()

    f= open(f"{nimi}.txt","w+", encoding="UTF-8")
    f.write(f"Nimi: {nimi}\n")
    f.write(f"Level: {playerlevel} ({xp_current}XP/{xp_needed}XP)\n")
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
    sleep(1)
    print("")
    print(f"Salvestatud {nimi}.txt'ina")
    main()
    
    
main()