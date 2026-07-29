#!/bin/bash

ROL="SysAdmin Jr."
USUARIO_SISTEMA=$(whoami)

echo -n "¿En que tema vas a trabajar hoy?: "
read TEMA

echo "$USUARIO_SISTEMA tu rol es $ROL, elejiste trabajar para hoy $TEMA"	
