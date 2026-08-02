#!/bin/bash
# ==============================================================================
# Script: limpiar_archivos.sh
# Objetivo: Remover acentos, eñes y espacios invisibles de archivos JSON y YAML
# ==============================================================================

echo "Iniciando proceso de sanitización en .json y .yaml..."

# Recorremos todos los archivos que terminen en .json o .yaml
for archivo in *.json *.yaml; do

    # Verificamos que el archivo realmente exista
    if [ -f "$archivo" ]; then
        echo "Procesando: $archivo"

        # Aplicamos sed in-place (-i) para hacer los cambios directamente en el archivo
        sed -i \
            -e 's/\xc2\xa0/ /g' \
            -e 's/á/a/g; s/é/e/g; s/í/i/g; s/ó/o/g; s/ú/u/g' \
            -e 's/Á/A/g; s/É/E/g; s/Í/I/g; s/Ó/O/g; s/Ú/U/g' \
            -e 's/ñ/n/g; s/Ñ/N/g' \
            "$archivo"
    fi

done

echo "----------------------------------------"
echo "¡Sanitización completada con éxito!"
