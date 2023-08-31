# Analiza hribov in poti v Sloveniji
### Projektna naloga pri predmetu Uvod v programiranje
#### Shranil sem naslednje podatke:
- ime hriba,
- gorovje v katerem leži hrib,
- nadmorska višina hriba,
- vrsta cilja (npr. koča, vrh ...)
- število poti, ki vodijo na posamezni hrib,
- višinska razlika po vsaki poti,
- zahtevnost poti,
- predviden čas hoje. 

#### Hipoteze in vprašanja na katera bom poskušil odgovoriti z analizo podatkov:
1. V katerem gorovju imajo hribi v povprečju največ poti?
2. Višji hribi imajo zahtevnejše poti.
3. Če je na cilju koča, do cilja vodi več poti, kot do ciljev brez koč.
4. V Julijskih alpah je največ zahtevnejših poti.
5. Na hribe s povprečno manjšo zahtevnostjo poti vodi več poti.
6. Koliko višinskih metrov se v povprečju naredi v eni minuti?
7. Pot z večjo višinsko razliko je v povprečju težja.

#### Repozitorij `Hribi_projektna_naloga` vsebuje naslednje datoteke:
* V datoteki [Vsi_hribi.html](..Hribi_projektna_naloga/Vsi_hribi.html) je shranjena spletna stran na kateri je seznam vseh hribov, ki sem jih analiziral.
* Iz zgornje spletne strani sem izluščil imena hribov in nato v mapo [Strani_hribov](..Hribi_projektna_naloga/Strani_hribov) v formatu `.html` shranil spletne strani vseh hribov.
* V mapi [Strani_poti](..Hribi_projektna_naloga/Strani_poti) so, prav tako v formatu `.html`, shranjene spletne strani z opisi vseh poti, ki vodijo na hribe iz prejšnje mape.
* S skripto [izlušči_hribe.py](..Hribi_projektna_naloga/izlušči_hribe.py) sem opravil vso predpripravo podatkov, ki sem jih uporabil v analizi.
* Ko skripto poženemo dobimo poleg prej opisanih datotek še `.csv` datoteki s podatki o hribih - [hribiAnaliza.csv](..Hribi_projektna_naloga/hribiAnaliza.csv) in poteh - [potiAnaliza.csv](..Hribi_projektna_naloga/potiAnaliza.csv).
* Ti dve datoteki sem nato uporabil pri [analizi podatkov](..Hribi_projektna_naloga/Analiza_podatkov.ipynb).
