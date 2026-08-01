#!/bin/bash

mkdir -p apuntes
FECHA=$(date)

echo -n "ingresa un tema: "
read TEMA

echo -n "ingresa el comando o nota a guardar: "
read NOTA

echo "[$FECHA] $TEMA: $NOTA" >> apuntes/notas.txt
cat apuntes/notas.txt
