from random import *
from time import *
import os
import re
def clear():
    os.system("cls")
def start():
    global debug
    global kas
    global turn2
    global turn
    debug = 0
    turn2 = 0
    turn = 0
    kas = "[0]"
    main()
# Sätti see '1', et muuta allolevaid muutujaid kergesti :)

def main():
    global kas
    global debug
    global turn2
    global playerchance
    global playerhp
    global playerhp2
    global playerattack
    global playerdef
    global playerdex
    global playermana
    global playerint
    global playerluck
    global playerdef2
    global ruu_def
    global relv_min
    global relv_max
    if turn2 > 0:
        playerdef2 = ruu_def + playerdef
        playerchance = playerluck+50
        playerhp = 75*(playerlevel*1.25)
        playerhp2 = playerhp;
        playerattack = 1*(playerlevel*1.25)
        playerdef = 1*(playerlevel*1.25)
        playerdex = 1*(playerlevel*1.25)
        playermana = 1*(playerlevel*1.25)
        playerint = 1*(playerlevel*1.25)
        playerluck = 1*(playerlevel*1.25)
        relv_min = (playerattack*2.0)
        relv_max = (playerattack*2.5)
    s = None
    clear()
    print(f"""
                    =====================
                    Seiklused Joodikutega
                        (Kalevipoeg)
                         Rougelike
                    =====================
          -----------------------------------------------                    
                    Salvestamine   - TEST1 (done)
                 Laadmise test     - TEST2 (done)
                 New char test     - TEST3 (done)
                 Combat test       - TEST4 (done)
                 Looting test      - TEST5
          Armory and equiping test - TEST6
                 Story             - TEST7
                 Map?              - TEST8
          -----------------------------------------------
                Debug mode {kas}     - DEBUG (done)
                 Player test       - PLAYER
                 Tunnustused       - CREDITS (done)
          -----------------------------------------------
          Versioon: WIP
                 
""")
    s = input().upper()
    if s == "TEST1":
        turn2 += 1
        clear()
        savetest()
    if s == "TEST2":
        clear()
        turn2 += 1
        loadtest()
    if s == "TEST3":
        os.system("cls")
        turn2 += 1
        newchar()
    if s == "TEST4":
        os.system("cls")
        atrituubid()
    if s == "TEST5":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "TEST6":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "TEST7":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "TEST8":
        os.system("cls")
        print("Veel pole midagi siin ):")
        sleep(5)
        main()
    if s == "DEBUG":
        os.system("cls")
        if debug == 0:
            debug = 1
            kas = "[1]"
        elif debug == 1:
            debug = 0
            kas = "[0]"
        main()
    if s == "PLAYER":
        print(f"nimi: {nimi}")
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
        print("")
        input("Enter")
        main()
        
    if s == "CREDITS":
        clear()
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
            print(f"Level up! \nLeveled to {playerlevel}!!")
            xp_needed = round(xp_needed+(playerlevel*100.275),0)
            level_up_check()
def savetest():
    global nimi
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

    f = open(f"SAVE/{nimi}.txt","w+", encoding="UTF-8")
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
    
    global nimi
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
    playerspecials = None

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

    f = open(f"SAVE/{nimi}.txt","w+", encoding="UTF-8")
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
    
    global nimi
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
                        playerdef = float(s[0])
                        a2 = a3[2]
                        s = re.findall(r"[-+]?\d*\.\d+|\d+", a2)
                        playerdef2 = float(s[0])

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
                        playerdex = float(s[0])
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
                        playerattack = float(s[0])
            
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
                        playermana = float(s[0])
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
                        playerint = float(s[0])
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
                        playerluck = float(s[0])
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
                        playerlevel = float(a2[1])
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
                        relv_min = float(s[0])
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
                        relv_max = float(relv_max.replace("-", ""))
               
                    
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
                        ruu_def = float(s[0])
               
                    
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
                        xp_current = float(s[0])
                                


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
                            xp_needed = float(s[1])
                                

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
                        playerskoor = float(a2[1])

            lines += 1 #eritab line'e
    
    if debug == 1:
        print(f"nimi: {nimi}")
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
        print("")
        input("Enter")
    level_up_check()
    main()
def atrituubid():
    global playerdmg
    global playerchance
    global playerlevel
    global playerhp
    global playerhp2
    global relv_min
    global relv_max
    global enemylevel
    global enemyhp
    global enemyhp2
    global enemyattack
    global enemychance
    global enemydef
    global enemydex
    global enemyluck
    global headshot
    global leg
    global balls
    global juhtus
    global juhtus1
    global turn
    global kas
    global debug
    global turn
    global playerchance
    global playerhp
    global playerhp2
    global playerattack
    global playerdef
    global playerdex
    global playermana
    global playerint
    global playerluck
    global playerdef2
    global ruu_def
    
    playerchance = playerluck+50
    playerhp = 100+50*(playerlevel*0.25)
    playerhp2 = playerhp;
    playerattack = 1*(playerlevel*0.25)
    playerdef = 1*(playerlevel*0.25)
    playerdex = 1*(playerlevel*0.25)
    playermana = 1*(playerlevel*0.25)
    playerint = 1*(playerlevel*0.25)
    playerluck = 1*(playerlevel*0.25)
    juhtus = ""
    juhtus1 = ""
    #Enemy
    enemylevel = playerlevel + randint(-2,2)
    enemyhp = 50*(enemylevel*0.25)
    enemyhp2 = enemyhp;
    enemyattack = round((randint(1,10)/5*enemylevel),0)
    enemydex = enemylevel*2
    enemydef = enemylevel*2
    enemyluck = enemylevel-2
    enemychance = enemyluck+50
    #attackid
#1/10000000
    randomnimi()

def muldsilma ():
    relv_min = relv_min*0.9
    relv_max = relv_max*0.9
    pass
    #Vastaste kalibreerimine
def randomnimi():
    global nimevalik
    global enemyattack
    global enemydex
    global enemyluck
    global enemyname
    global headshot
    global leg
    global balls
    nimevalik = ["Paganlane", "Rammus Paganlane", "Tempokas Paganlane","Joobes Paganlane"]
    enemyname = nimevalik[randint(0,3)]
    print(enemyname)
    if enemyname == "Paganlane":
        pass

    elif enemyname == "Rammus Paganlane":
        enemyattack += 2
        enemydex -= 1
   
    elif enemyname == "Tempokas Paganlane":
        enemydex += 3
        enemyattack -= 1
    
    elif enemyname == "Joobes Paganlane":
        if randint(1,200)==1:
            enemyattack += 4000
            enemyluck -= 49
        else:
            randomnimi()
        #enemydmg = randint(enemyattack*0.8,enemyattack*1.2)
    headshot = 1.5*enemyattack
    leg = 0.75*enemyattack
    balls = 5*enemyattack 
    combat()
    
def combat():
    
    global nimi
    global playerattack#Player
    global playerdef
    global playerdex
    global playermana
    global playerint
    global playerspecials
    global playerlevel
    global playerchance
    global playerhp
    global playerhp2
    global relv_min
    global relv_max
    global nimevalik#Vastased
    global enemylevel
    global enemychance
    global enemyhp
    global enemyhp2
    global xp_current
    global enemyattack
    global enemydmg
    global enemydex
    global enemyluck
    global juhtus
    global juhtus1
    global turn
    global playerskoor
    global enemydef
    clear()
    if turn==0:
        if playerdex >= enemydex:
            print("Sa lähed esimesena")
            turn +=1
        else:
            print("Sa lähed teisena")
            turn +=1
            combat1()
    if playerhp <= 0:
        print("Sa surid")
        sleep(5)
        main()
    elif enemyhp <= 0:
        aaaah = randint(1,100)*playerlevel
        aaaah2 = randint(1,10)*enemylevel
        print("Sa võitsid")
        print(f"+{aaaah} XP")
        print(f"+{aaaah2} skoor")
        playerskoor += aaaah2
        xp_current += aaaah
        level_up_check()
        sleep(5)
        main()
            
    print(f"""

 Vastane: {enemyname}
 HP: ({enemyhp}/{enemyhp2})


 Sina: {juhtus}
 Vastane: {juhtus1}


 Sina: {nimi} 
 HP: ({playerhp}/{playerhp2})

[1] - Nõrgalt    | +25% Pihtasaamis võimalus | -25% Tugevam löök
[2] - Keskmiselt | Tavaline löök
[3] - Tugevalt   | +25% Tugevam löök         | -25% Pihtasaamis võimalus

""")
    test = input("Kui tugevasti lööd? ").upper()
    if test == "1":            
        playerdmg = randint(relv_min*10,relv_max*10)/10
        playerdmg = playerdmg*75/100
        playerchance = playerchance + 25
        if (randint(0,100)<=playerchance):               
            juhtus = f"Sa slappisid teda vastu põske | -{playerdmg}dmg" #Nõrgalt
            if (playerdmg-enemydef)<=0:
                juhtus1 = "Su ema karjus su peale ja sa ehmatasid"
            else:
                enemyhp = enemyhp - (playerdmg-enemydef)
        else:
            juhtus = "Su ema karjus su peale ja sa ehmatasid"
        combat1()
    elif test == "2":
        playerdmg = randint(relv_min*10,relv_max*10)/10
        if (randint(0,100)<=playerchance):               
            juhtus = f"Sa lõid teda | -{playerdmg}dmg"  #Keskmiselt
            if (playerdmg-enemydef)<=0:
                juhtus1 = "Sa komistasid"
            else:
                enemyhp = enemyhp - (playerdmg-enemydef)
        else:
            juhtus = "Sa komistasid"
        combat1()
    elif test == "3":
        playerdmg = randint(relv_min*10,relv_max*10)/10
        playerdmg = playerdmg + 25
        playerchance = playerchance*75/100
        if (randint(0,100)<=playerchance):               
            juhtus = f"Sa kogusid kõik oma mehise jõu ja antsid enda parima löögi mida Eesti näinud on | -{playerdmg}dmg" #Tugevalt
            if (playerdmg-enemydef)<=0:
                juhtus1 = "Suure jõu kogumiseajal, punnitasid liiga kõvasti, sittudes endale püksi"
            else:
                enemyhp = enemyhp - (playerdmg-enemydef)
        else:
            juhtus = "Suure jõu kogumiseajal, punnitasid liiga kõvasti, sittudes endale püksi"
        combat1()
            
def combat1():
    
    global nimi
    global playerattack#Player
    global playerdef
    global playerdef2
    global playerdex
    global playermana
    global playerint
    global playerspecials
    global playerlevel
    global playerchance
    global playerhp
    global playerhp2
    global relv_min
    global relv_max
    global nimevalik#Vastased
    global enemylevel
    global enemychance
    global enemyhp
    global enemyhp2
    global enemyattack
    global enemydmg
    global enemydex
    global enemyluck
    global headshot
    global leg
    global balls
    global juhtus
    global juhtus1
    clear()    
            
    if (randint(1,1000000) == 1):
        enemydmg = randint(balls*800,balls*1200)/1000
        if (randint(0,100)<=enemychance):               
            juhtus1 = f"Sa said jaladega munadesse :c | -{enemydmg}dmg"  #Balls
            if (enemydmg-playerdef2)<=0:
                juhtus1 = "Ta lõi mööda"
            else:
                playerhp = playerhp - (enemydmg-playerdef2)
            
        else:
            juhtus1 = "Ta lõi mööda"
    elif (randint(1,2) == 1):
        enemydmg = randint(leg*800,leg*1200)/1000
        if (randint(0,100)<=enemychance):               
            juhtus1 = f"Ta lõi jalga sind | -{enemydmg}dmg"  #Leg
            if (enemydmg-playerdef2)<=0:
                juhtus1 = "Ta tegi backflippi ja failis"
            else:
                playerhp = playerhp - (enemydmg-playerdef2)

        else:
            juhtus1 = "Ta tegi backflippi ja failis"
    else:
        enemydmg = randint(headshot*800,headshot*1200)/1000
        if (randint(0,100)<=enemychance):               
            juhtus1 = f"Ta 360 noskoop sind otse näkku | -{enemydmg}dmg"  #Headshot
            if (enemydmg-playerdef2)<=0:
                juhtus1 = "Ema helistas talle ja küsis 'Kus ta stringid on?'"
            else:
                playerhp = playerhp - (enemydmg-playerdef2)
        else:
            juhtus1 = "Ema helistas talle ja küsis 'Kus ta stringid on?'"
    playerhp = round(playerhp,0)
    enemyhp = round(enemyhp,0)

    combat()
        
        



start()
