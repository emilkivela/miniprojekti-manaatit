## Manaattien LaTeX-viitetyökalu
- [Backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/jannekoi_ad_helsinki_fi/EYn4NiHQI7NOrNhXnwcYWz4BjzSH1-En9Xs1Cre1dXYCrw?e=KMDOtW)

## Käyttöohje
- Luo virtuaaliympäristö komennolla ``` python3 -m venv venv ```
- Siirry virtuaaliympäristöön komennolla ``` source venv/bin/activate ```
- Asenna riippuvuudet komennolla ``` pip install -r requirements.txt" ```
- Lataa postgresql
- Luo sinne tietokanta reftool
- Luo tietokantaa taulut schema.sql:n mukaisesti
- Käynnistä sovellus ajamalla komento ``` flask -A app/app run ``` juurihakemistossa

## Testit
- Suorita testit virtuaaliympäristössä ajamalla komento ``` pytest ``` juurihakemistossa

## Definition of Done
- Pushed to GitHub
- Fills out acceptance criteria
- Tested manually and automatically

Sovellus on testattavissa [Azuressa](https://manaatit.azurewebsites.net/)
