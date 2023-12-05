#!/bin/bash

# käynnistetään gunicorn-palvelin taustalle
gunicorn --bind=0.0.0.0 --timeout 600 startup:app &

# odotetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
i=0
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' 0.0.0.0:8000/ping)" != "404" ]];
  do sleep 1;
  ((i++))
  if [ $i -gt 60 ]
  then
    exit 1
  fi
done

# suoritetaan testit
robot --variable SERVER:0.0.0.0:8000 tests

status=$?

# pysäytetään gunicorn-palvelin portissa 8000
kill $(lsof -t -i:8000)

exit $status
