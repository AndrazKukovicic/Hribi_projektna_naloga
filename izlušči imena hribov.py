import re

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

#Iz seznama blokov, ki vsebujejo imena hribov izlušči ime hriba v obliki, ki se uporablja v povezavi do spletne strani hriba.
def imena_hribov():
    bloki = poisci_bloke()
    hribi =  []
    vzorec_hrib = r'href="(.*)"><b'
    for blok in bloki:
        hrib = re.search(vzorec_hrib, blok, flags=re.DOTALL)
        hribi.append(hrib.group(1))
    return hribi

hribčki = imena_hribov()
print(hribčki)