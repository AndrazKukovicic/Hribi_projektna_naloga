import re
import os
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

bloki = bloki_podatki_pot()
print(bloki)