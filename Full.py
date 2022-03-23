from random import *
from time import *
import os
debug = 0
# Sätti see '1', et muuta allolevaid muutujaid kergesti :)

def main():
    os.system('cls')
    print(f"""
                    =====================
                    Seiklused Joodikutega
                    =====================
                    
                 Salvestamise test - TEST1 (done)
                 Laadmise test     - TEST2 (done)
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
    else:
        print(f"Vigane Käsk {s}")
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
    global relva_info
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
    global relva_info
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
    import re
    debug = 1
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
    global relva_info
    global playerskoor
    lines = 1
    nimi = input("Sisesta oma eelmise characteri nimi: ")
    f = open(f"SAVE/{nimi}.txt","r", encoding="UTF-8")
    for line in f:
        lines += 1
        for i in range(200):
            a1 = list(f)
            a1 = [line.rstrip('\n') for line in f]
            a1 = line.split()
            a2 = a1[1]
            playername = a2;
            #nimi (korras)
            
            # def (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [4]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerdef = s[0]
                        a2 = a3[2]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerdef2 = s[0]

                # dex(korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [5]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerdex = s[0]
                #atk (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [3]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerattack = s[0] 
            
                # mana(korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [6]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playermana = s[0] 
                # int (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [7]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerint = s[0]
                # luck(korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [8]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[1]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerluck = s[0]
                # specials (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [9]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        playerspecials = a2[1]
                # level(korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                # .-.
                line_numbers = [1]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        playerlevel = a2[1]
                # relv
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [11]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        relv = a2[1]
            
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [11]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        relva_info = a2[2]
               
                # relv_min (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [3]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[2]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        relv_min = s[0]
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [3]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = a3 = line.split();
                        a2 = a2[2]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        relv_max = s[1]
                        relv_max = relv_max.replace("-", "")
               
                    
                # ruu (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [12]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        ruu = a2[1]
               
                    
                # ruu_def (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [12]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        ruu_def = s[0]
               
                    
                # aksessuaar (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [13]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        aksessuaar = a2[1]
               
                    
                # aksessuaar_info (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [13]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        aksessuaar_info = a2[2]
                
               
                    
                # xp_current (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [1]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        a2 = a2[2]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        xp_current = s[0]
                                


                # xp_needed (korras)
                with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                    line_numbers = [1]
                    a1 = []
                    for i, line in enumerate(fp):
                        if i in line_numbers:
                            a1.append(line.strip())
                            a2 = str(a1[0])
                            a2 = line.split()
                            a2 = a2[2]
                            s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                            xp_needed = s[1]
                                

                # class (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [15]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        playerclass = a2[1]
                # skoor (korras)
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [16]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        playerskoor = a2[1]

            lines += 1 #eritab line'e
    if debug == 1:
        try:
            
            print(f"playerattack: {playerattack}")
            print(f"playerdef: {playerdef}")
            print(f"playerdef2: {playerdef2}")
            print(f"playerdex: {playerdex}")
            print(f"playermana: {playermana}")
            print(f"playerint: {playerint}")
            print(f"playerluck: {playerluck}")
            print(f"playerspecials: {playerspecials}")
            print(f"playerlevel: {playerlevel}")
            print(f"relv: {relv}")
            print(f"relv_min: {relv_min}")
            print(f"relv_max: {relv_max}")
            print(f"ruu: {ruu}")
            print(f"ruu_def: {ruu_def}")
            print(f"aksessuaar: {aksessuaar}")
            print(f"aksessuaar_info: {aksessuaar_info}")
            print(f"xp_current: {xp_current}")
            print(f"xp_needed: {xp_needed}")
            print(f"playerclass: {playerclass}")
            print(f"playerskoor: {playerskoor}")
        except:
            print("midagi on katki")
        



main()
