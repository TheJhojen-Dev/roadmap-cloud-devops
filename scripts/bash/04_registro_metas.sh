#!/bin/bash

mkdir -p registros

echo -n "Escribe tu meta del día: "
read META

echo "$META" >> registros/metas.txt

echo "--- Lista de metas actualizadas ---"
cat registros/metas.txt
