Analiza potrošnje električne energije u EU

Ovaj projekt analizira potrošnju električne energije u državama Europske unije korištenjem otvorenih podataka Eurostata. Sustav obuhvaća prikupljanje podataka iz CSV i JSON izvora, njihovu obradu i integraciju, pohranu u SQLite bazu podataka, izradu REST API-ja te analizu i vizualizaciju podataka u Jupyter Notebooku.

Projekt uključuje:

obradu energetskih i populacijskih podataka

integraciju heterogenih izvora (CSV + JSON)

bazu podataka (SQLite)

REST servis (Flask)

analizu ukupne potrošnje i potrošnje po stanovniku

grafove i trendove

Struktura projekta

Pzap_projekt.ipynb – glavni notebook i dokumentacija (obrada, integracija, analiza, grafovi)

eurostat_energy.csv – energetski podaci (CSV)

eurostat_population.json – populacija (JSON)

eu_energy.db – SQLite baza

api.py – Flask REST API


Pokretanje REST servisa

Prije pokretanja potrebno je imati instaliran Python 3.10 ili noviju verziju te biblioteke pandas i flask.

Instalacija biblioteka:
pip install pandas flask

Pokretanje REST servisa iz direktorija projekta:
python api.py

Nakon pokretanja servis je dostupan na adresi:
http://127.0.0.1:5000

Opis REST servisa

REST servis omogućuje dohvat podataka iz baze eu_energy.db koja sadrži integrirane energetske i populacijske podatke.

Implementirane rute:

Dohvat svih država
GET /countries
Vraća popis svih dostupnih država u bazi.

Dohvat svih zapisa
GET /energy
Vraća sve integrirane zapise (država, godina, potrošnja, populacija).

Dohvat podataka za određenu državu
GET /energy/<country>
Primjer:
/energy/DE
Vraća sve zapise za odabranu državu.

Dohvat podataka za državu i godinu
GET /energy/<country>/<year>
Primjer:
/energy/DE/2020
Vraća zapise za odabranu državu i godinu.

LINK NA REPOZITORI:
https://github.com/aborjan1/Analiza-potro-nje-elektri-ne-energije-po-dr-avama-EU
