#!/bin/bash

mkdir -p bitacoras

FECHA=$(date)

echo -n "Ingresa tu nombre: "
read NOMBRE

echo -n "¿Actividad realizada hoy?: "
read ACTIVIDAD

echo "[$FECHA] $NOMBRE: $ACTIVIDAD" >> bitacoras/diario.txt
cat bitacoras/diario.txt
