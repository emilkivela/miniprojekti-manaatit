#!/bin/bash

process_exists () {
  if [[ $(ps --no-headers -p $1) ]]
  then
    true
  else
    false
  fi
}

kill_if_running () {
  if process_exists $1
  then
    kill $1
  fi
}

SERVER_ADDRESS=0.0.0.0:8000
export SECRET_KEY=test

# käynnistetään gunicorn-palvelin taustalle
gunicorn --bind=$SERVER_ADDRESS --timeout 600 startup:app &
gunicorn_pid=$!
trap "kill_if_running $gunicorn_pid" EXIT HUP INT TERM

# odotetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
i=0
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' $SERVER_ADDRESS/ping)" != "404" ]]
do
  sleep 1
  ((i++))
  if ! process_exists $gunicorn_pid
  then
    exit 1
  fi
  if [[ $i > 5 ]]
  then
    kill_if_running $gunicorn_pid
    exit 1
  fi
done

# suoritetaan testit
robot --variable SERVER:$SERVER_ADDRESS tests

status=$?

# pysäytetään gunicorn-palvelin
kill_if_running $gunicorn_pid

exit $status
