#!/bin/bash

mkdir -p tickets
FECHA=$(date +%Y-%m-%d)

echo -n "Nombre del servicio afectado: "
read SERVICIO

echo -n "Nivel de prioridad: "
read PRIORIDAD

echo -n "Descripción breve del problema: "
read DESCRIPCION_PROBLEMA

echo "-----------------------------------" >> tickets/historial.txt
echo -e "SERVICIO:$SERVICIO\nPRIORIDAD:$PRIORIDAD\nDESCRIPCION:$DESCRIPCION_PROBLEMA" >> tickets/historial.txt

cat tickets/historial.txt
