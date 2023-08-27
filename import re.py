import re 
import os
def izlusci_podatke(blok):
    hrib = {}
    vzorec1 = re.compile(
            r';"><h1>(?P<ime>.*?)</h1',
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
    hrib["Višina"] = najdba3["visina"]
    hrib["Število poti"] = najdba4["steviloP"]
    hrib["Vrsta cilja"] = najdba5["vrsta"]


    
    return hrib
def izlusci_bloke_hribi():
    bloki = []
    os.chdir("Strani_hribov")
    for i in range(2107):
        
        with open(f"{i}.html", encoding='utf-8') as dat:
            celo_besedilo = dat.read()
            vzorec_bloka1 = re.compile(
                r'<div class="naslov1"><div style="float:left(?P<besedilo>.*?)<b>Opis gore:</b>', 
                flags=(re.DOTALL|re.IGNORECASE)
            )
            for najdba in re.finditer(vzorec_bloka1, celo_besedilo):
            # vzorec_bloka2 = re.compile(
            #     r'<table class="TPoti" id="poti">'
            #     r'.*?'
            #     r'</table>',
            #     flags=re.DOTALL,
            # )
            
                bloki.append(najdba['besedilo'])
    os.chdir("..")
    return bloki
def izluscii_vse_hribi():
    podatki_hribi = []
    bloki = izlusci_bloke_hribi()
    for blok in bloki:
        hrib = izlusci_podatke(blok)
        podatki_hribi.append(hrib)
    return podatki_hribi

podatki = izluscii_vse_hribi()
print(podatki)

