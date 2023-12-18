## Manaattien LaTeX-viitetyökalu
![GHA workflow badge](https://github.com/emilkivela/miniprojekti-manaatit/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/emilkivela/miniprojekti-manaatit/graph/badge.svg)](https://codecov.io/gh/emilkivela/miniprojekti-manaatit)

Sovellus on testattavissa [Azuressa](https://manaatit.azurewebsites.net/)
- [Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/jannekoi_ad_helsinki_fi/EYn4NiHQI7NOrNhXnwcYWz4BjzSH1-En9Xs1Cre1dXYCrw?e=KMDOtW)
- [Loppuraportti](https://helsinkifi-my.sharepoint.com/:w:/g/personal/jannekoi_ad_helsinki_fi/EenuGPcJRIhJnO9G3LCXppoB_KGNxMeJWV5whKufFTE97Q?e=PBMowh)

## Sovelluksen käynnistäminen paikallisesti
1. Luo virtuaaliympäristö komennolla ``` python3 -m venv venv ```
2. Siirry virtuaaliympäristöön komennolla ``` source venv/bin/activate ```
3. Asenna riippuvuudet komennolla ``` pip install -r requirements.txt ```
4. Tallenna .env-tiedostoon juurihakemistossa ympäristömuuttujien määrittelyt:
   ```
   AZURE_POSTGRESQL_CONNECTIONSTRING='host=localhost:5432 dbname=tietokannannimi user=käyttäjätähän password=salasanatähän'
   SECRET_KEY=jokusecretkeytähän
   ```
   - ``` tietokannannimi ``` on tätä sovellusta varten omalle koneellesi luomasi tietokannan nimi
   - ``` käyttäjätähän ``` on käyttäjänimesi PostGreSQL:ssä omalla koneellasi
   - ``` salasanatähän ``` on kyseisen käyttäjän salasana
   - (Jos et ole vielä asettanut PostGreSQL:ssä salasanaa, niin sen voi tehdä SQL-komennolla ``` ALTER USER käyttäjätähän WITH PASSWORD 'salasanatähän'; ```)
   - ``` jokusecretkeytähän ``` on mikä vain vapaasti valitsemasi merkkijono
5. Käynnistä sovellus ajamalla komento ``` flask -A app/app run ``` juurihakemistossa

## Sovelluksen käynnistäminen Azuressa
1. Käytä Azure App Servicesiä, joka sisältää PostqreSQL-tietokannan
2. Siirry Deployment Centeriin, lisää Git repositorio ja tallenna
3. Suorita Sync
4. Siirry Azuressa: Configuration -> General settings ja lisää Startup Command ``` gunicorn --bind=0.0.0.0 --timeout 600 startup:app ```
5. Käynnistä palvelin

## Testit
- Suorita yksikkötestit virtuaaliympäristössä ajamalla komento ``` pytest ``` juurihakemistossa
- Suorita Robot framework -testit käynnistämällä ensin sovellus yhdellä komentorivillä komennolla ``` flask -A app/app run ``` (aivan kuten yllä) ja ajamalla sitten toisella komentorivillä samaan tapaan virtuaaliympäristössä sovelluksen juurihakemistossa komento ``` robot tests ```
  - (ChromeDriverista tai muista Drivereista ei tarvitse enää huolehtia itse, sillä nykyään Selenium asentaa tarvittavan Driverin ja kaiken sen tarvitseman automaattisesti)
- Suorita Pylint-tarkastukset ajamalla virtuaaliympäristössä komento ``` pylint app tests ``` projektin juurihakemistossa
- Muodosta haarautumakattavuusraportti ajamalla virtuaaliympäristössä komento ``` coverage run --branch -m pytest; coverage html ``` projektin juurihakemistossa

## Definition of Done
- Pushed to GitHub
- Fills out acceptance criteria
- Tested manually and automatically

