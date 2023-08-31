# Analiza hribov in poti v Sloveniji
### Projektna naloga pri predmetu Uvod v programiranje
V projektni nalogi sem obdelal in predstavil podatke o hribih in poteh nanje, ki sem jih pridobil s spletnega portala __[hribi.net](https://www.hribi.net)__. 
<br><br>
#### Shranil sem naslednje podatke:
- ime hriba,
- gorovje v katerem leži hrib,
- nadmorska višina hriba,
- vrsta cilja (npr. koča, vrh ...)
- število poti, ki vodijo na posamezni hrib,
- višinska razlika po vsaki poti,
- zahtevnost poti,
- predviden čas hoje. 
*** 
#### Hipoteze in vprašanja, ki sem si jih postavil:
1. V katerem gorovju imajo hribi v povprečju največ poti?
2. Višji hribi imajo zahtevnejše poti.
3. Če je na cilju koča, do cilja vodi več poti, kot do cilja brez koče.
4. V Julijskih alpah je največ zahtevnejših poti.
5. Na hribe s povprečno manjšo zahtevnostjo poti vodi več poti.
6. Koliko višinskih metrov se v povprečju naredi v eni minuti?
7. Pot z večjo višinsko razliko je v povprečju težja.
***
#### Repozitorij `Hribi_projektna_naloga` vsebuje naslednje datoteke:
* V datoteki __[Vsi_hribi.html](Vsi_hribi.html)__ je shranjena spletna stran na kateri je seznam vseh hribov, ki sem jih analiziral.
* Iz zgornje spletne strani sem izluščil imena hribov in nato v mapo __[Strani_hribov](Strani_hribov)__ v formatu `.html` shranil spletne strani vseh hribov.
* V mapi __[Strani_poti](Strani_poti)__ so, prav tako v formatu `.html`, shranjene spletne strani z opisi vseh poti, ki vodijo na hribe iz prejšnje mape.
* S skripto __[izlušči_hribe.py](izlušči_hribe.py)__ sem opravil vso predpripravo podatkov, ki sem jih uporabil v analizi.
* Ko skripto poženemo dobimo poleg prej opisanih datotek še `.csv` datoteki s podatki o hribih - __[hribiAnaliza.csv](hribiAnaliza.csv)__ in poteh - __[potiAnaliza.csv](potiAnaliza.csv)__.
* Ti dve datoteki sem nato uporabil pri analizi podatkov, ki je narejena v datoteki __[Analiza_podatkov.ipynb](Analiza_podatkov.ipynb)__.
