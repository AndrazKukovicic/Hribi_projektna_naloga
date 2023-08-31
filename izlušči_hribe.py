import re
import requests
import os
import csv


# Iz shranjene spletne strani z vsemi hribi izlušči bloke z imeni hribov in jih shrani v seznam.
def poisci_bloke():
    bloki = []
    with open("Vsi_hribi.html") as dat:
        celo_besedilo = dat.read()
        vzorec_bloka = re.compile(
            r'colspan="2"><a' 
            r".*?" 
            r'><b',
            flags=re.DOTALL
        )
        for najdba in vzorec_bloka.finditer(celo_besedilo):
            bloki.append(celo_besedilo[najdba.start() : najdba.end()])
    return bloki


# Iz seznama blokov, ki vsebujejo imena hribov izlušči ime hriba v obliki, 
# ki se uporablja v povezavi do spletne strani hriba.
def imena_hribov():
    bloki = poisci_bloke()
    hribi =  []
    vzorec_hrib = r'href="(.*)"><b'
    for blok in bloki:
        hrib = re.search(vzorec_hrib, blok, flags=re.DOTALL)
        hribi.append(hrib.group(1))
    return hribi


# Shrani spletne strani vseh hribov v mapo Strani_hribov.
def shrani_hribe():
    ImenaHribovURL = imena_hribov()
    ImenaHribovURL.remove('/gora/plesivec/11/2377') #ročno zbrisal, ker so se pojavljali večrat in delali težave
    ImenaHribovURL.remove('/gora/plesivec/11/2377') 
    ImenaHribovURL.remove('/gora/plesivec/11/300')
    ImenaHribovURL.remove('/gora/orleska_draga/26/3642')
    os.chdir("Strani_hribov")
    print(os.getcwd())
    for stran in ImenaHribovURL:
        url = f"https://www.hribi.net{stran.strip()}"
        odziv = requests.get(url)
    
        if odziv.status_code == 200:
            print(url)
            with open(f"{ImenaHribovURL.index(stran)}.html", "w", encoding='utf-8') as s:
                s.write(odziv.text)
        else:
            print("Prišlo je do napake")
    os.chdir("..")


# Iz spletnih strani izlušči bloke iz katerih nato izluščimo podatke o hribu.
def izlusci_bloke_hribi():
    bloki = []
    os.chdir("Strani_hribov")
    for i in range(2107):
        
        with open(f"{i}.html", encoding='utf-8') as dat:
            celo_besedilo = dat.read()
            vzorec_bloka1 = re.compile(
                r'<div class="naslov1"><div style="float:left'
                r'.*?'
                r'<b>Opis', 
                flags=re.DOTALL
            )
            for najdba in vzorec_bloka1.finditer(celo_besedilo):
            
            
                bloki.append(celo_besedilo[najdba.start() : najdba.end()])
    os.chdir("..")
    return bloki


# Izlušči bloke s seznamom vseh poti za posamezni hrib.
def izlusci_bloke_poti():
    bloki = []
    os.chdir("Strani_hribov")
    for i in range(2107):
        
        with open(f"{i}.html", encoding='utf-8') as dat:
            celo_besedilo = dat.read()
            vzorec_bloka2 = re.compile(
                r'<table class="TPoti" id="poti">'
                r'.*?'
                r'</table>',
                flags=re.DOTALL,
            )
            for najdba2 in vzorec_bloka2.finditer(celo_besedilo):
                
                    bloki.append(celo_besedilo[najdba2.start() : najdba2.end()])
    os.chdir("..")
    return bloki


# Iz bloka s podatki o posameznem hribu izlušči podatke in jih shrani v slovar.
def izlusci_podatke(blok):
    hrib = {}
    vzorec1 = re.compile(
            r'left;"><h1>(?P<ime>.*?)</h1',
            flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec2 = re.compile(
        r'<b>Gorovje:</b> <a class="moder" href=".*?">(?P<gorovje>.*?)</a>',
        flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec3 = re.compile(
        r'<b>Višina:</b>(?P<visina>.*?)&nbsp',
        flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec4 = re.compile(
        r'href="#poti">(?P<steviloP>\d+)'
    )
    vzorec5 = re.compile(
        r'><b>Vrsta:</b>(?P<vrsta>.*?)</div>'
    )
    najdba1 = re.search(vzorec1, blok)
    najdba2 = re.search(vzorec2, blok)
    najdba3 = re.search(vzorec3, blok)
    najdba4 = re.search(vzorec4, blok)
    najdba5 = re.search(vzorec5, blok)

    hrib["Ime"] = str(najdba1["ime"])
    hrib["Gorovje"] = najdba2["gorovje"]
    hrib["Višina"] = int(najdba3["visina"].strip())
    hrib["Število poti"] = int(najdba4["steviloP"])
    hrib["Vrsta cilja"] = najdba5["vrsta"].strip().split(', ')

    return hrib


# Poišči imena za linke do poti, naredi seznam poti.
def poisci_poti():
    bloki = izlusci_bloke_poti()
    poti =  []
    vzorec_pot = re.compile(
        r'class="tdG"><a href="/izlet(?P<pot>.*?)">', 
        flags=re.DOTALL
        )
    for blok in bloki:
        najdba = vzorec_pot.finditer(blok)
        for izlet in najdba:
            if '/izlet' + izlet['pot'] in poti:
                 continue
            else:
                poti.append('/izlet' + izlet['pot'])
    return poti


# Shrani spletne strani vseh poti v mapo Strani_poti.
def shrani_poti():
    ImenaPotiURL = poisci_poti()
    os.chdir("Strani_poti")
    for stran in ImenaPotiURL:
        url = f"https://www.hribi.net{stran.strip()}"
        odziv = requests.get(url)
        if odziv.status_code == 200:
            print(url)
            with open(f"p{ImenaPotiURL.index(stran)}.html", "w", encoding='utf-8') as s:
                s.write(odziv.text)
        else:
            print("Prišlo je do napake")
    os.chdir("..")


#  Izlušči blok s podatki o poti in vrne seznam blokov.
def bloki_podatki_pot():
    bloki = []
    os.chdir("Strani_poti")
    for i in range(6907):
         with open(f"p{i}.html", encoding='utf-8') as dat:
            celo_besedilo = dat.read()
            vzorec_bloka1 = re.compile(
                r"<b>Cilj:</b> <a class"
                r".*?"
                r"<b>Zemljevid:</b>",
                flags=(re.DOTALL|re.IGNORECASE)
            )
            for najdba1 in vzorec_bloka1.finditer(celo_besedilo):
                bloki.append(celo_besedilo[najdba1.start() : najdba1.end()])
    os.chdir("..")
    return bloki


#  Izlušči podatke o poti in vrne slovar.
def izlusci_podatke_pot(blok):
    pot = {}
    vzorec1 = re.compile(
        r'<b>Cilj:</b> <a class="moder" href="(.+?)">(?P<ime>.*?) \(\d',
        flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec2 = re.compile(
        r'po poti:</b> (?P<visinska>.*?) m<',
        flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec3 = re.compile(
        r'<b>Zahtevnost:</b> (?P<zahtevnost>.*?)<',
        flags=(re.DOTALL|re.IGNORECASE)
    )
    vzorec4 = re.compile(
        r'<b>Čas hoje:</b>(?P<cas>.*?)<'
    )
    najdba1 = re.search(vzorec1, blok)
    najdba2 = re.search(vzorec2, blok)
    najdba3 = re.search(vzorec3, blok)
    najdba4 = re.search(vzorec4, blok)
    pot["Ime"] = najdba1["ime"]
    pot["Visinska_razlika"] = najdba2["visinska"]
    pot["Zahtevnost"] = najdba3["zahtevnost"]
    pot["Čas"] = najdba4["cas"].strip()
    return pot


# Izlušči podatke o vseh hribih in vrne seznam slovarjev.
def izlusci_vse_hribi():
    podatki_hribi = []
    bloki = izlusci_bloke_hribi()
    for blok in bloki:
        hrib = izlusci_podatke(blok)
        podatki_hribi.append(hrib)
    return podatki_hribi


# Izlušči podatke o vseh poteh in vrne seznam slovarjev.
def izlusci_vse_poti():
    podatki_poti = []
    bloki = bloki_podatki_pot()
    for blok in bloki:
        pot = izlusci_podatke_pot(blok)
        podatki_poti.append(pot)
    return podatki_poti


# Pripravi csv datoteko s podatki o hribih.
def izpisi_podatke_hribi():
    podatki = izlusci_vse_hribi()
    with open("hribi.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Ime", "Gorovje", "Višina", "Število_poti", "Vrsta_cilja"])
        for hrib in podatki:
            writer.writerow([hrib["Ime"], hrib["Gorovje"], hrib["Višina"], hrib["Število poti"], hrib["Vrsta cilja"]])


# Pripravi csv datoteko s podatki o poteh
def izpisi_podatke_poti():
    podatki = izlusci_vse_poti()
    with open("poti.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Ime", "Višinska_razlika", "Zahtevnost", "Čas"])
        for hrib in podatki:
            writer.writerow([hrib["Ime"], hrib["Visinska_razlika"], hrib["Zahtevnost"], hrib["Čas"]])


# Popravi zapis časa (pretvori v minute) v csv datoteki s potmi.
def popravi_cas(vhodna, izhodna):
    with open(vhodna, encoding='utf-8') as vh:
        with open(izhodna, 'w', encoding='utf-8') as izh:
            vrste = [vrsta.strip() for vrsta in vh]
            for vrsta in vrste:
                if vrste.index(vrsta) == 0:
                    ime, razlika, zahtevnost, cas = re.split(';',  vrsta)
                    izh.write( f"{ime};{razlika};{zahtevnost};{cas}\n")
                if vrsta == '':
                    continue
                else:
                    ime, razlika, zahtevnost, cas = re.split(';',  vrsta)
                    if 'h' in cas and 'm' not in cas:
                        vzorecUre = re.compile(
                            r'(?P<ure>\d+?) h'
                        )
                        najdbaUre = vzorecUre.search(cas)
                        ure = int(najdbaUre["ure"])
                        skupaj = ure * 60
                        izh.write(f"{ime};{razlika};{zahtevnost};{skupaj}\n")
                    if 'h' in cas and 'm' in cas:
                        vzorecUre = re.compile(
                            r'(?P<ure>\d+?) h'
                        )
                        najdbaUre = vzorecUre.search(cas)
                        ure = int(najdbaUre["ure"])
                        vzorecMinute = re.compile(
                            r'(?P<minute>\d+?) min'
                        )
                        najdbaminute = vzorecMinute.search(cas)
                        minute = int(najdbaminute['minute'])
                        skupaj = ure * 60 + minute
                        izh.write(f"{ime};{razlika};{zahtevnost};{skupaj}\n")
                    if 'h' not in cas and 'm' in cas:
                        vzorecMinute = re.compile(
                            r'(?P<minute>.*?) min'
                        )
                        najdbaminute = vzorecMinute.search(cas)
                        minute = int(najdbaminute['minute'])
                        skupaj = minute
                        izh.write(f"{ime};{razlika};{zahtevnost};{skupaj}\n")


# Popravi zapis podatkov o hribih, tako da so ločeni s ; in brez praznih vrstic.
def popraviVrstocilja(vhodna, izhodna):
    with open(vhodna, encoding='utf-8') as vh:
        with open(izhodna, 'w', encoding='utf-8') as izh:
            vrste = [vrsta.strip() for vrsta in vh]
            for vrsta in vrste:
                if vrste.index(vrsta) == 0:
                    ime, gorovje, visina, stPoti, vrstaCilja = re.split(';',  vrsta)
                    izh.write(f"{ime};{gorovje};{visina};{stPoti};{vrstaCilja}\n")
                    continue
                if vrsta == '':
                    continue
                else:
                    ime, gorovje, visina, stPoti, vrstaCilja = re.split(';',  vrsta)
                    vCiljaPop = vrstaCilja[1:-1]
                    izh.write(f"{ime};{gorovje};{visina};{stPoti};{vCiljaPop}\n")



#--------------------------------------poženi--------------------------------------

# izpisi_podatke_hribi()
# izpisi_podatke_poti()
# popravi_cas('poti.csv', 'potiAnaliza.csv')
# popraviVrstocilja('hribi.csv', 'hribiAnaliza.csv')

#----------------------------------------------------------------------------------