#!/bin/bash

SERVER_ADDRESS=0.0.0.0:8000

# käynnistetään gunicorn-palvelin taustalle
gunicorn --bind=$SERVER_ADDRESS --timeout 600 startup:app &
gunicorn_pid=$!

# odotetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
i=0
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' $SERVER_ADDRESS/ping)" != "404" ]]
do
  sleep 1
  ((i++))
  if [[ $i -gt 60 ]]
  then
    if [[ $(ps --no-headers -p $gunicorn_pid) ]]
    then
      kill $gunicorn_pid
    fi
    exit 1
  fi
done

# suoritetaan testit
robot --variable SERVER:$SERVER_ADDRESS tests

status=$?

# pysäytetään gunicorn-palvelin
if [[ $(ps --no-headers -p $gunicorn_pid) ]]
then
  kill $gunicorn_pid
fi

exit $status
