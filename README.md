## Manaattien LaTeX-viitetyökalu
- [Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/jannekoi_ad_helsinki_fi/EYn4NiHQI7NOrNhXnwcYWz4BjzSH1-En9Xs1Cre1dXYCrw?e=KMDOtW)

## Sovelluksen käynnistäminen paikallisesti
1. Luo virtuaaliympäristö komennolla ``` python3 -m venv venv ```
2. Siirry virtuaaliympäristöön komennolla ``` source venv/bin/activate ```
3. Asenna riippuvuudet komennolla ``` pip install -r requirements.txt ```
4. Aseta ympäristömuuttuja ``` export AZURE_POSTGRESQL_CONNECTIONSTRING='host=localhost:5432 dbname=tietokannannimi user=kayttajatanne password=salasanatanne' ``` (tietokannannimi on tätä sovellusta varten omalle koneellesi luomasi tietokannan nimi, kayttajatanne on käyttäjänimesi PostGreSQL:ssä omalla koneellasi ja salasanatanne on kyseisen käyttäjän salasana. Jos et ole vielä asettanut PostGreSQL:ssä salasanaa, niin sen voi tehdä SQL-komennolla "ALTER USER kayttajatanne WITH PASSWORD 'salasanatanne';")
5. Luo tietokantataulut ajamalla app-hakemistossa komennot ``` flask db init && flask db migrate -m "initial migration" && flask db upgrade ```
6. Käynnistä sovellus ajamalla komento ``` flask -A app/app run ``` juurihakemistossa

(Ensimmäisen käynnistyskerran jälkeen riittää sovelluksen käynnistämiseksi tehdä vain vaiheet 2, 4 ja 6.)

## Sovelluksen käynnistäminen Azuressa
- Käytä Azure App Servicesiä, joka sisältää PostqreSQL-tietokannan
- Siirry Deployment Centeriin, lisää Git repositorio ja tallenna
- Suorita Sync
- Siirry Azuressa: Configuration -> General settings ja lisää Startup Command ``` gunicorn --bind=0.0.0.0 --timeout 600 startup:app ```
- Käynnistä palvelin
- Siirry SSH-konsoliin ja luo tietokantataulut komennoilla ``` flask db init && flask db migrate -m "initial migration" && flask db upgrade ```

## Testit
- Suorita testit virtuaaliympäristössä ajamalla komento ``` pytest ``` juurihakemistossa

## Definition of Done
- Pushed to GitHub
- Fills out acceptance criteria
- Tested manually and automatically

Sovellus on testattavissa [Azuressa](https://manaatit.azurewebsites.net/)
