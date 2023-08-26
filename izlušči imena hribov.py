import re
import requests
import os

#Iz shranjene spletne strani z vsemi hribi izlušči bloke z imeni hribov in jih shrani v seznam.
def poisci_bloke():
    bloki = []
    with open("Vsi_hribi.html") as dat:
        celo_besedilo = dat.read()
        vzorec_bloka = re.compile(
            r'colspan="2"><a' r".*?" r'><b',
            flags=re.DOTALL,
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

# hribčki = imena_hribov()
# print(hribčki)

# Shrani spletne strani vseh hribov v mapo Strani_hribov.
# ImenaHribovURL = imena_hribov()
# ImenaHribovURL.remove('/gora/orleska_draga/26/3642')
# ImenaHribovURL.remove('/gora/plesivec/11/300') #ročno zbrisal
# ImenaHribovURL.remove('/gora/plesivec/11/2377')
# ImenaHribovURL.remove('/gora/plesivec/11/2377')
# os.chdir("Strani_hribov")
# print(os.getcwd())
# for stran in ImenaHribovURL:
#     url = f"https://www.hribi.net{stran.strip()}"
#     odziv = requests.get(url)
    
#     if odziv.status_code == 200:
#         print(url)
#         with open(f"{ImenaHribovURL.index(stran)}.html", "w", encoding='utf-8') as s:
#             s.write(odziv.text)
#     else:
#         print("Prišlo je do napake")
# os.chdir("..")

# isto kot poišči bloke: izlušči bloke iz katerih anto izluščimo podatke o hribu
def izlusci_bloke_hribi():
    bloki = []
    os.chdir("Strani_hribov")
    for i in range(2106):
        
        with open(f"{i}.html", encoding='utf-8') as dat:
            celo_besedilo = dat.read()
            vzorec_bloka1 = re.compile(
                r'<div class="naslov1"><div style="float:left' 
                r'.*?' 
                r'<b>Opis gore:</b>', 
                flags=re.DOTALL
            )
            # vzorec_bloka2 = re.compile(
            #     r'<table class="TPoti" id="poti">'
            #     r'.*?'
            #     r'</table>',
            #     flags=re.DOTALL,
            # )

            for najdba1 in vzorec_bloka1.finditer(celo_besedilo):
                
                    bloki.append(celo_besedilo[najdba1.start() : najdba1.end()])
    os.chdir("..")
    return bloki

# izlušči bloke s seznamom vseh poti za nek hrib
def izlusci_bloke_poti():
    bloki = []
    os.chdir("Strani_hribov")
    for i in range(2106):
        
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
    hrib["Ime"] = najdba1["ime"]
    hrib["Gorovje"] = najdba2["gorovje"]
    hrib["Višina"] = int(najdba3["visina"].strip())
    hrib["Število poti"] = int(najdba4["steviloP"])
    hrib["Vrsta cilja"] = najdba5["vrsta"].strip().split(', ')


    
    return hrib


# poišči imena za linke do poti, naredi seznam poti
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

# ImenaPotiURL = poisci_poti()

# os.chdir("Strani_poti")
# print(os.getcwd())
# for stran in ImenaPotiURL:
#     url = f"https://www.hribi.net{stran.strip()}"
#     odziv = requests.get(url)
    
#     if odziv.status_code == 200:
#         print(url)
#         with open(f"p{ImenaPotiURL.index(stran)}.html", "w", encoding='utf-8') as s:
#             s.write(odziv.text)
#     else:
#         print("Prišlo je do napake")
# os.chdir("..")

# Izlušči blok s podatki o poti in vrne seznam blokov.
def bloki_podatki_pot():
    bloki = []
    os.chdir("Strani_poti")
    for i in range(6906):
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

# Izlušči podatke o poti in vrne slovar.
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
def izluscii_vse_hribi():
    podatki_hribi = []
    bloki = izlusci_bloke_hribi()
    for blok in bloki:
        hrib = izlusci_podatke(blok)
        podatki_hribi.append(hrib)
    return podatki_hribi

podatki = izluscii_vse_hribi()
print(len(podatki))

def izlusci_vse_poti():
    podatki_poti = []
    bloki = bloki_podatki_pot()
    for blok in bloki:
        pot = izlusci_podatke_pot(blok)
        podatki_poti.append(pot)
    return podatki_poti
podatki1 = izlusci_vse_poti()
print(len(podatki1))