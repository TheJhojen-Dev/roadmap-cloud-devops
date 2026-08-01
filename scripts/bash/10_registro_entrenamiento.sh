#!/bin/bash

mkdir -p entrenamientos
FECHA=$(date +%Y-%m-%d)

echo -n "Ejercicio principal realizado hoy (ej: Flexiones, Dominadas, Fondos): "
read EJERCICIO

echo -n "Número de repeticiones completadas: "
read REPETICIONES

echo "-------------------------------------------------------" >> entrenamientos/diario_fitness.txt
echo "[$FECHA] Ejercicio: $EJERCICIO | Volumen: $REPETICIONES" >> entrenamientos/diario_fitness.txt
cat entrenamientos/diario_fitness.txt
