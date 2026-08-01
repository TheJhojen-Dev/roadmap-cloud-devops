#!/bin/bash

FECHA=$(date +%H:%M:%S)
USUARIO=$(whoami)
IP=$(hostname -I)

mkdir -p registros_red

echo -n "ingresa mensaje de estado: "
read MENSAJE_RED

echo "[$FECHA] [$USUARIO@$IP]: $MENSAJE_RED" >> registros_red/estado.log
cat registros_red/estado.log
