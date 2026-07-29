#!/bin/bash

ESTADO="En proceso"

HOY=$(date +%Y-%m-%d)

echo -n "Escribe tu nombre: "
read USUARIO

echo "Hola $USUARIO. Fecha: $HOY | Estado del estudio: $ESTADO"
