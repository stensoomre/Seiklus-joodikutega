from random import *
from time import *
import os
import re
def clear():
    os.system("cls")
def clearacc(): #Uus tegelane
    
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
    global munt
    f = open(f"SAVE/{nimi}.txt","w+", encoding="UTF-8")
    f.write(f"")
    f.close()
    pass
    
def start():
    
    global debug
    global kas
    global turn2
    global turn
    global munt
    debug = 0
    turn2 = 0
    turn = 0
    munt = 0
    kas = "[0]"
    main()
    
# Sätti see '1', et muuta allolevaid muutujaid kergesti :)

def main(): #Menu screen
    
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
    s = None
    clear()
    vaste = input(str("""
                        ======================
                             "Kalevipoeg"
                        ======================
              Aga mis siis kui üks joodik ütles teisele, et ei
              ─────────────────────────────────────────────────
              
                     Mängi             - ALUSTA
                     Jätka progressi   - LAE
                     
              ─────────────────────────────────────────────────
              
                     Tunnustused       - TUBLID
                     
              ─────────────────────────────────────────────────
              Versioon: 0.1.1
          
""")).upper()
    if vaste == "ALUSTA":
        clear()
        alustamine()
       #Ma ausalt ei mäleta järjekorda aga noh siit see läheb ):
    elif vaste == "LAE":
        clear()
        loadtest()
    elif vaste == "TUBLID":
        clear()
        print(f"""

                    Pea-Arendaja: Sten Soomre
                    Kaas-Arendaja: Erik Teppan
        
                    
                    Tublid olid: Ardo, mitte keegi teine ;)
                                (isegi)
                        (aitäh, et poodi tulid)
    """)
        input("Enter")
        main()
    elif vaste != "Neeger":
        print("Vale vaste")
        main()
def level_up_check():
    
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
    global relv_min # Plus mine kergelt öeldud perse - Ardo
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
    global munt
    global xp_current # Global on supreme
    global xp_needed # Global on supreme
    global playerlevel # Global on supreme    global playerattack3
    global playerdef3
    global playerdex3
    global playermana3
    global playerint3
    global playerluck3
    global playerhp
    global playerhp2
    global playerdef2
    if xp_current>xp_needed: # Kui xp on suurem kui xp max
            xp_current -= xp_needed # võta maha
            playerlevel += 1 # level up :)
            #########################
            playerattack3 = playerattack;
            playerdef3 = playerdef;
            playerdex3 = playerdex;
            playermana3 = playermana;
            playerint3 = playerint;
            playerluck3 = playerluck;
            #########################
            playerchance = round((playerluck3+(playerluck+50)),0)
            if playerchance >=95:
                playerchance = 95
            playerhp = round((75*(playerlevel*1.05)),0)
            playerhp2 = playerhp;
            playerattack += 1
            playerdef += 1
            playerdef2 += playerdef
            playerdex += 1
            playermana += 1
            playerint += 1
            playerluck += 1
            relv_min = round((playerattack*2.0),0)
            relv_max = round((playerattack*2.5),0)
            print(f"Level up! \nLeveled to {playerlevel}!!")
            xp_needed = round(xp_needed+(playerlevel*100.275),0)
            level_up_check()
def savetest(): #salvestamis seadistus
    
    global nimi
    global playerattack
    global playerdef
    global playerdex
    global playermana
    global playerint
    global playerluck
    global playerattack3
    global playerdef3
    global playerdex3
    global playermana3
    global playerint3
    global playerluck3
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
    global munt
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
    f.write(f"Ruu: {ruu} +({ruu_def} DEF)\n")
    f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
    f.write("---------------------\n")
    f.write(f"Klass: {playerclass}\n")
    f.write(f"Skoor: {playerskoor}\n")
    f.write(f"munt: {munt}\n")
    f.close()
    sleep(1)
    print("")
    print(f"Salvestatud {nimi}.txt'ina")
    sleep(4)
    alustamine2()

    
    
def newchar(): #Uue char seadistus / Valimine
    
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
    global munt
    global playerhp
    global playerhp2
    
    nimi = input("Siseta nimi: ")
    soov = input("""
 Mis klassitüüpina tahad mängida?
 
 [1] - Mõõgamees
 [2] - Vibumees
 [3] - Maag
 [4] - Nõid
 [5] - Laps
 [6] - Talumees
 [7] - Mario (Võib tekitada paradoxi?) 
 [8] - Kalevipoeg
 [9] - Joodik 
 [10] - Mentaalse hälvega

""")
    if soov == "1":
        playerclass = "Mõõgamees"
        playerattack = 2
        playerdef = 1
        playerdex = 0
        playermana = 0
        playerint = 0
        playerluck = 1
        playerspecials = "Oskus"
        munt = 2
        relv = "Ekskalibur"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Kivist-võetud\""
        ruu = "Rüü"
        ruu_def = 5
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Saapanõõrid"
    elif soov == "2":
        playerclass = "Vibumees"
        playerattack = 1
        playerdef = 0
        playerdex = 4
        playermana = 0
        playerint = 1
        playerluck = 2
        playerspecials = "Täpsus"
        munt = 0
        relv = "Vibu"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Nooltega\""
        ruu = "Noolehoidla"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Binokkel"
    elif soov == "3":
        playerclass = "Maag"
        playerattack = 1
        playerdef = 1
        playerdex = 1
        playermana = 4
        playerint = 4
        playerluck = 0
        playerspecials = "Maagia"
        munt = 0
        relv = "Kepp"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Kummist\""
        ruu = "Keep"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Vunts"
    elif soov == "4":
        playerclass = "Nõid"
        playerattack = 1
        playerdef = 1
        playerdex = 1
        playermana = 4
        playerint = 4
        playerluck = 0
        playerspecials = "Kasutu"
        munt = 0
        relv = "Luud"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Puidust\""
        ruu = "Keep"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Nõia-Müts"
    elif soov == "5":
        playerclass = "Laps"
        playerattack = 3
        playerdef = 0
        playerdex = 0
        playermana = 0
        playerint = 0
        playerluck = 4
        playerspecials = "Lollkas"
        munt = 15 #taskuraha
        relv = "Lego"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Ai\""
        ruu = "Mähkmed"
        ruu_def = 4
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Pulgakomm"
    elif soov == "6":
        playerclass = "Talumees"
        playerattack = 2
        playerdef = 1
        playerdex = 1
        playermana = 1
        playerint = 1
        playerluck = 1
        playerspecials = "Harimisoskus"
        munt = 0
        relv = "Kõlbas"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Vanakoolne\""
        ruu = "Traksid"
        ruu_def = 4
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Sigar"
    elif soov == "7":
        playerclass = "Mario" #Supreme race
        playerattack = 100
        playerdef = 100
        playerdex = 100
        playermana = 100
        playerint = 1000 #aju geenius
        playerluck = 100
        playerspecials = "Tarkus"
        munt = 1000
        relv = "IT-for-Dummies"
        relv_min = 10
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 200
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Oppa\""
        ruu = "Plot-armor"
        ruu_def = 20
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Naljaraamat"
    elif soov == "8":
        playerclass = "Kalevipoeg"
        playerattack = 10
        playerdef = 1
        playerdex = 1
        playermana = 1
        playerint = 1
        playerluck = 1
        playerspecials = "Legend"
        munt = 10
        relv = "Mõõk"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Päris\""
        ruu = "Uskumus"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Saapad"
    
    elif soov == "9":
        playerclass = "Joodik"
        # stats
        playerattack = 1
        playerdef = 1
        playerdex = 1
        playermana = 1
        playerint = 1
        playerluck = 1
        playerspecials = "Alati_purjus"
        munt = 0 # pension
        relv = "Lauaviin"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Ainult_õige_eestlane_suudab_seda_tõsta\""
        ruu = "Alkohol"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Lauaviin"
    elif soov == "10":
        playerclass = "Hälvik"
        # stats
        playerattack = 1
        playerdef = 1
        playerdex = 1
        playermana = 1
        playerint = 1
        playerluck = 1
        playerspecials = "Hälve"
        munt = 1000
        relv = "Sittajunn"
        relv_min = 1
        relv_min = relv_min+(playerattack*2.5)
        relv_max = 2
        relv_max = relv_max+(playerattack*2.5)
        relva_info = "\"Mida_kuradit\""
        ruu = "Higi"
        ruu_def = 2
        playerdef2 = ruu_def + playerdef
        aksessuaar = "Pangakaart"
    else:
        print("Vale vaste")
        sleep(2)
    aksessuaar_info = None
    playerlevel = 1
    playerhp = round((75*(playerlevel*1.05)),0)
    playerhp2 = playerhp;
    if playerlevel == 1:
        xp_needed = 100
        xp_current = 0#round(randint(1,100000),0)
    if xp_current>xp_needed:
        level_up_check()
    playerskoor = 0
    munt2 = 0
    try:
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
        f.write(f"Ruu: {ruu} +({ruu_def} DEF)\n")
        f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
        f.write("---------------------\n")
        f.write(f"Klass: {playerclass}\n")
        f.write(f"Skoor: {playerskoor}\n")
        f.write(f"munt: {munt}\n")
        f.close()
        sleep(1)
        print("")
        print(f"Salvestatud {nimi}.txt'ina")
        clear()
        sleep(4)
        print("Nüüd lae oma tegelane sisse :)")
        sleep(4)
        main()
    except:
        try:
            os.mkdir("SAVE")
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
            f.write(f"Ruu: {ruu} +({ruu_def} DEF)\n")
            f.write(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}\n")
            f.write("---------------------\n")
            f.write(f"Klass: {playerclass}\n")
            f.write(f"Skoor: {playerskoor}\n")
            f.write(f"munt: {munt}\n")
            f.close()
            sleep(1)
            print("")
            print(f"Salvestatud {nimi}.txt'ina")
            sleep(4)
            clear()
            print("Nüüd lae oma tegelane sisse :)")
            sleep(4)
            main()
        except:
            pass
def loadtest(): #Laadimise seadistus
    
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
    global munt
    global playerhp
    global playerhp2
    global playerchance
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
            with open(f"SAVE/{nimi}.txt","r", encoding="UTF-8") as fp:
                line_numbers = [17]
                a1 = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        a1.append(line.strip())
                        a2 = str(a1[0])
                        a2 = line.split()
                        munt = float(a2[1])

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
        print(f"munt: {munt}")
        
        print("")
        input("Enter")
    playerluck3 = playerluck;
    playerchance = round((playerluck3+(playerluck+50)),0)
    playerhp = round((75*(playerlevel*1.05)),0)
    playerhp2 = playerhp;
    level_up_check()
    alustamine2()
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
    global playerskoor
    global playerint
    global playerluck
    global playerdef2
    global ruu_def
    juhtus = ""
    juhtus1 = ""
    #Enemy
    enemylevel = playerlevel + randint(-2,2)
    if enemylevel <= 0:
        enemylevel = playerlevel + randint(1,2)
    enemyhp = 50*(enemylevel*0.25)
    enemyhp2 = enemyhp;
    enemyattack = round((5*enemylevel/randint(1,4)),0)
    enemydex = enemylevel*2
    enemydef = enemylevel*2
    enemyluck = enemylevel-2
    enemychance = round(((enemyluck*0.8)+50),0)
    if enemychance >=95:
        enemychance = 95
    #attackid
#1/10000000
    if playerskoor >= 200000:
        randomnimi2()
    else:
        randomnimi()

def muldsilma ():
    relv_min = relv_min*0.9
    relv_max = relv_max*0.9
    pass
    #Vastaste kalibreerimine
def randomnimi2(): #Boss seadistus
    
    global nimevalik
    global enemyattack
    global enemydex
    global enemyluck
    global enemyname
    global headshot
    global leg
    global balls   
    nimevalik = ["Vanapagan"]
    enemyname = nimevalik[randint(0,len(nimevalik)-1)]
    if enemyname == "Vanapagan":
        enemyattack *= 2
        enemydex *= 1
        #enemydmg = randint(enemyattack*0.8,enemyattack*1.2)
    headshot = 2.5*enemyattack
    leg = 1.75*enemyattack
    balls = 10*enemyattack 
    combat()
def randomnimi(): #Käsilased
    
    global nimevalik
    global enemyattack
    global enemydex
    global enemyluck
    global enemyname
    global headshot
    global leg
    global balls   
    nimevalik = ["Paganlane", "Rammus Paganlane", "Tempokas Paganlane","Joobes Paganlane","Seiklev COOP"]
    enemyname = nimevalik[randint(0,len(nimevalik)-1)]

    if enemyname == "Rammus Paganlane":
        enemyattack += 2
        enemydex -= 1
   
    elif enemyname == "Tempokas Paganlane":
        enemydex += 3
        enemyattack -= 1
    
    elif enemyname == "Joobes Paganlane":
        if randint(1,200)==1:
            enemyattack += 4000
            enemyluck -= 49
        
    elif enemyname == "Seiklev COOP":
            shopreset()
            pood()
        #enemydmg = randint(enemyattack*0.8,enemyattack*1.2)
    headshot = 1.5*enemyattack
    leg = 0.75*enemyattack
    balls = 5*enemyattack 
    combat()
    
def combat(): #Player combat   
    
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
    global munt
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
        input("""

        Sa surid,
        sa valmistusid meile pettumust, kuidas sa hakkama ei saanud,
        me kõik uskusime sinusse, mis sinu punastest stringidest saab?
        
        Kas sa tõesti ei mõista, miks return on parem, kui global?
        Loodan, et Põrgus pole ühtegi ALKO1000 (TEHNILISELT POOD)
        
        Isegi su vend on sinust parem,        
        Mine proovi uuesti SA VÄIKE ALAARENENUD SEINAPÕRKEGA NÄPITUD SITANÄKERDIS!!!!!

        PS: proovi uuesti :)
        
        Enter
""")
        clearacc()
        main()
    elif enemyhp <= 0:
        if enemyname == "Vanapagan": 
            clear()                   #FIN
            input("""
            Sa said hakkama, üleaegade pole keegi saanud hakkama, Vanapagana tappmisega,
            sa oled inspiratsioon meile kõigile ja meie kangelane, äitäh et läbisid selle raske teekonna. 
            
            Aaaja ma ei tutvustanud ennast, ega ju?
            Tere, minu nimi on Mario Metshein meeldiv tutvuda!
            Kõike paremat ja puhka, kui puhke aeg on :)
            
                        
            Enter
            """)
            clearacc()
            main()
    
        else:
            aaaah = randint(1,100)*playerlevel
            aaaah2 = randint(1,100)*enemylevel
            munt += round((randint(1,20)+(0.8*enemylevel)),0)
            print("Sa võitsid")
            print(f"+{aaaah} XP")
            print(f"+{aaaah2} skoor")
            print(f"Sul on {munt} münti")
            playerskoor += aaaah2
            xp_current += aaaah
            level_up_check()
            sleep(2)
            alustamine2()
            #UI
    print(f"""

 Vastane: {enemyname}                  
 HP: ({enemyhp}/{enemyhp2}) | LEVEL: {enemylevel}
 Võimalus pihta saada: {playerchance}%



 Sina: {juhtus}
 Vastane: {juhtus1}


 Sina: {nimi}      
 HP: ({playerhp}/{playerhp2}) | LEVEL: {playerlevel} 
 Võimalus pihta saada: {enemychance}%


[1] - Nõrgalt    | +25% Pihtasaamis võimalus | -25% Tugevam löök
[2] - Keskmiselt | Tavaline löök
[3] - Tugevalt   | +25% Tugevam löök         | -25% Pihtasaamis võimalus

""")
    test = input("Kui tugevasti lööd? ").upper()   #Mängija turn
    if test == "1":            
        playerdmg = randint(relv_min*100000000000,relv_max*100000000000)/100000000000
        playerdmg = playerdmg*75/100
        playerchance1 = (playerchance + 25);
        if (randint(0,100)<=playerchance1):               
            juhtus = f"Sa slappisid teda vastu põske | -{playerdmg}dmg" #Nõrgalt
            if (playerdmg-enemydef)<=0:
                juhtus1 = "Su ema karjus su peale ja sa ehmatasid"
            else:
                enemyhp = enemyhp - (playerdmg-enemydef)
        else:
            juhtus = "Su ema karjus su peale ja sa ehmatasid"
        combat1()
    elif test == "2":
        playerdmg = randint(relv_min*100000000000,relv_max*100000000000)/100000000000
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
        playerdmg = randint(relv_min*100000000000,relv_max*100000000000)/100000000000
        playerdmg = playerdmg + 25
        playerchance1 = (playerchance*75/100);
        if (randint(0,100)<=playerchance1):               
            juhtus = f"Sa kogusid kõik oma mehise jõu ja antsid enda parima löögi mida Eesti näinud on | -{playerdmg}dmg" #Tugevalt
            if (playerdmg-enemydef)<=0:
                juhtus1 = "Suure jõu kogumiseajal, punnitasid liiga kõvasti, sittudes endale püksi"
            else:
                enemyhp = enemyhp - (playerdmg-enemydef)
        else:
            juhtus = "Suure jõu kogumiseajal, punnitasid liiga kõvasti, sittudes endale püksi"
        combat1()
    else:
        juhtus = "Sa ei teinud sittagi :)"
        combat1()
            
def combat1(): # Enemy seadistus
    
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
            
    if (randint(1,1000000) == 1):           #Vastase turn
        enemydmg = randint(balls*8000000000,balls*12000000000)/10000000000
        if (randint(0,100)<=enemychance):               
            juhtus1 = f"Sa said jaladega munadesse :c | -{enemydmg}dmg"  #Balls
            if (enemydmg-playerdef2)<=0:
                juhtus1 = "Ta lõi mööda"
            else:
                playerhp = playerhp - (enemydmg-playerdef2)
            
        else:
            juhtus1 = "Ta lõi mööda"
    elif (randint(1,2) == 1):
        enemydmg = randint(leg*8000000000,leg*12000000000)/10000000000
        if (randint(0,100)<=enemychance):               
            juhtus1 = f"Ta lõi jalga sind | -{enemydmg}dmg"  #Leg
            if (enemydmg-playerdef2)<=0:
                juhtus1 = "Ta tegi backflippi ja failis"
            else:
                playerhp = playerhp - (enemydmg-playerdef2)

        else:
            juhtus1 = "Ta tegi backflippi ja failis"
    else:
        enemydmg = randint(headshot*8000000000,headshot*12000000000)/10000000000
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
        
def pood(): #Alko (Pood) seadistus
    
    clear()
    global nimi
    global playerattack
    global playerdef
    global playerdef2
    global playerdex
    global playerhp
    global playerhp2
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
    global munt
    global item1
    global item2
    global item3
    global item4
    price1, price2, price3, price4 = 15*playerlevel, 10*playerlevel, 15*playerlevel, 5*playerlevel
    
    print(f"""
                             ============
                               ALKO1000
                             ============
 Ardo Metssalu
        "Jälle sina, noh mis soovid?"



Rahakott: {munt} münti

[1] - {item1} | {price1} münti
[2] - {item2} | {price2} münti
[3] - {item3} | {price3} münti
[4] - {item4} |{playerhp}/{playerhp2}| {price4} münti

[TAGASI] - Viib sind tagasi

""")
    pood2 = input("Mida sa soovid osta?: ").upper()   #Mängija turn
    if pood2 == "1":
        if item1 == "ostetud":
            pood()
        else:
            if munt > price1:
               munt -= price1
               item1 = "ostetud"
               #Teeb midagi
               playerattack +=2
               pood()
            else:
                print("Sul pole piisavalt raha")
                sleep(2)
                pood()
    
    if pood2 == "2":
        if item2 == "ostetud":
            pood()
        else:
            if munt > price2:
               munt -= price2
               item2 = "ostetud"
               #Teeb midagi
               playerdef +=2
               playerdef2 +=2
               pood()
            else:
                print("Sul pole piisavalt raha")
                sleep(2)
                pood()

    if pood2 == "3":
        if item3 == "ostetud":
            pood()
        else:
            if munt > price3:
               munt -= price3
               item3 = "ostetud"
               #Teeb midagi
               playerdex +=2
               pood()
            else:
                print("Sul pole piisavalt raha")
                sleep(2)
                pood()
    if pood2 == "4":
        if item4 == "ostetud":
            pood()
        else:
            if munt > price4:
               munt -= price4
               item4 = "ostetud"
               #Teeb midagi
               playerhp = playerhp2;
               pood()
            else:
                print("Sul pole piisavalt raha")
                sleep(2)
                pood()
    if pood2 == "TAGASI":
        alustamine2()
    else:
        pood()
        
def shopreset():
    
    global item1
    global item2
    global item3
    global item4
    item1, item2, item3, item4 = "+2 ATK","+2 DEF","+2 DEX","Saa täis elud"      
        
def tsoon(): #Tsoonide seadistus    
    global playerskoor
    
    if playerskoor >= 200000: #200000 punkti tsoon kolme jaoks (väike hüpe) + boss fight
        print("Liigud surma")
    
    elif playerskoor >= 10000: #10000 punkti tsoon kahe jaoks (väike hüpe)
        print("Liigud kaugemale")
    
    else: #1000 punkti tsoon ühe jaoks
        print("Liigud edasi")
    sleep(3)
    clear()
    atrituubid()
                
def story(): #Story
    clear()
    print("""
                    Umbkautselt Eesti eepos nimega “Kalevipoeg”
                    ──────────────────────────────────────────
                                                     
         Sa oled hiljuti saanud üksikuseks meheks, kes rändab mööda Eesti ja aitab inimesi,
         aga nüüd pöördub sinu vastu Vanapagan ise ja tema käsilased,
         kes ründavad külasid varastavad kulda ja naiste punaseid stringe.
         
         Sinu ülesanne on haarata oma piip ja prillid ja omal valikul relv ja astuda teele,
         kus sa päästad naisi ja tapad patuseid paganaid, et saad Eesti vingemaks meheks ja istuda mängu lõpus
         kivist trooni peale (mis on külm) mida ümbritsevad naised ja nautida lihtsat elu.
         
         Kõike paremat, kangelane ja edukat rännakut,
         
         ELAGU ISAMAA!!!

""")
    input("Enter")
    clear()

def alustamine():
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
    global munt
    global playerhp
    global playerhp2
    global playerchance
    story()
    newchar()
    
def alustamine2(): #Story UI
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
    global munt
    global playerhp
    global playerhp2
    global playerchance
    clear()
    lmao = input(f"""

        Sina, {nimi} oled Kalevimaal.


        Mida sa teed?


        [1] - Liigu sügavamale
        [2] - Kaugel olen?
        [3] - Kus on Vanapagan?
        [4] - Näita mängija attritüüpe
        
        [5] - Salvesta progress


""")
    if lmao == "1":
        clear()
        tsoon()
    if lmao == "2":
        clear()
        print("Tundmatu tegelane - Võib öelda, et su teekond veel pikk.") #NPC
        sleep(2)
        alustamine2()
    if lmao == "3":
        clear()
        print("Tundmatu tegelane - Kuskil on, ei oska täpselt öelda, aga kui sa piisavalt tugevaks saad, ilmub ta ise.") #NPC
        sleep(2)
        alustamine2()
    if lmao == "4":
        clear()
        playerstats()
    if lmao == "5":
        clear()
        savetest()
    else:
        print(f"Vale vaste {lmao} ")
        sleep(2)
        alustamine2()
        
def playerstats():
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
        global munt
        global playerhp
        global playerhp
        print(f"Nimi: {nimi}")
        print(f"Level: {playerlevel} ({xp_current}XP/{xp_needed}XP)")
        print("---------------------")
        print(f"ATK: {playerattack} ({relv_min}-{relv_max})DMG")
        print(f"DEF: {playerdef} ({playerdef2})")
        print(f"DEX: {playerdex}")
        print(f"MANA: {playermana}")
        print(f"INT: {playerint}")
        print(f"LUCK: {playerluck}")
        print(f"SPECIALS: {playerspecials}")
        print("---------------------")
        print(f"RELV: {relv} {relva_info}")
        print(f"Ruu: {ruu} +({ruu_def} DEF)")
        print(f"AKSESSUAAR: {aksessuaar} {aksessuaar_info}")
        print("---------------------")
        print(f"Klass: {playerclass}")
        print(f"Skoor: {playerskoor}")
        print(f"munt: {munt}")
        print("")
        input("Enter")
        alustamine2()

start()

