#!/bin/bash

FECHA=$(date +%Y-%m-%d)
USUARIO=$(whoami)
EQUIPO=$(hostname)

echo -n "Describa que tarea principal realizara en esta sesion: "
read TAREA

echo "> Fecha: $FECHA"
echo "> Usuario: $USUARIO"
echo "> Equipo: $EQUIPO"
echo "> Tarea: $TAREA"
