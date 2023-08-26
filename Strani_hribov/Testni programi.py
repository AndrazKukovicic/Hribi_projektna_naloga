import re
import os
def bloki_podatki_pot():
    bloki = []
    os.chdir("Strani_poti")
    for i in range(10):
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

bloki = bloki_podatki_pot()
print(bloki)
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
pot = izlusci_podatke_pot(bloki[0])
print(pot)

def izlusci_vse_poti():
    podatki_poti = []
    bloki = izlusci_bloke_poti()
    for blok in bloki:
        pot = izlusci_podatke_pot(blok)
        podatki_poti.append(pot)
    return podatki_poti
podatki1 = izlusci_vse_poti()
print(podatki1)