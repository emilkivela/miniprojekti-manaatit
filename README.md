## Manaattien LaTeX-viitetyökalu
- [Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/jannekoi_ad_helsinki_fi/EYn4NiHQI7NOrNhXnwcYWz4BjzSH1-En9Xs1Cre1dXYCrw?e=KMDOtW)

## Sovelluksen käynnistäminen paikallisesti
- Luo virtuaaliympäristö komennolla ``` python3 -m venv venv ```
- Siirry virtuaaliympäristöön komennolla ``` source venv/bin/activate ```
- Asenna riippuvuudet komennolla ``` pip install -r requirements.txt" ```
- Lataa ja käynnistä PostgreSQL
- Aseta ympäristömuuttuja ``` export AZURE_POSTGRESQL_CONNECTIONSTRING='host=localhost:5432 dbname=manaatitdb user=kayttaja password=salasana' ```
- Luo tietokantataulut komennoilla ``` flask db init && flask db migrate -m "initial migration" && flask db upgrade ```
- Käynnistä sovellus ajamalla komento ``` flask -A app/app run ``` juurihakemistossa

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
