#!/usr/bin/env bash

ROOT_PATH="$(cd $(dirname ${BASH_SOURCE[0]})/.. && pwd)"

PYTHON="python"

USAGE_MSG="\
Usage:
  $ django.sh <commands>

List of <commands>:
- makemigrations
- migrate
- runserver"

function echo_help() {
  echo "$USAGE_MSG"
}

if [ $# -gt 0 ]; then
  case $* in
    makemigrations )
      CMD="$PYTHON manage.py makemigrations"
      ;;
    migrate )
      CMD="$PYTHON manage.py migrate"
      ;;
    runserver )
      CMD="$PYTHON manage.py runserver 0.0.0.0:8000"
      ;;
    -h | --help )
      CMD="echo_help"
      ;;
    * )
      CMD="$PYTHON manage.py $*"
      ;;
  esac
else
  CMD="echo_help"
fi

$CMD
