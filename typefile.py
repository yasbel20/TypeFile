# Autora: Yasbel Soto
# Git: https://github.com/yasbel20/TypeFile.git
# Este ejercicio es un TypeFile que muestra el contenido de un archivo e incerta el numero de linea

import sys      # Importamos sys para poder leer argumentos desde la línea de comandos
import os       # Importamos os para poder limpiar la pantalla

try:
    # Verificamos que se haya pasado al menos un argumento (el nombre del archivo)
    if len(sys.argv) < 2:
        raise ValueError("Debe indicar el nombre del archivo como argumento.")

    # Guardamos el nombre del archivo que se quiere leer (el primer argumento después del nombre del script)
    archivo_usuario = sys.argv[1]

    # Limpiamos la pantalla antes de mostrar el contenido
    # Si es Windows usa 'cls', si es Linux o Mac usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

    # Mostramos un pequeño mensaje antes de leer
    print("Leyendo el archivo:", archivo_usuario)
    print("-" * 20)

    # Abrimos el archivo en modo lectura con codificación UTF-8
    with open(archivo_usuario, 'r', encoding='utf-8') as archivo:
        # Usamos enumerate para contar líneas desde 1
        for numero_linea, contenido_linea in enumerate(archivo, start=1):
            # Imprimimos el número de línea con tres dígitos, seguido del contenido
            # El 'end' evita que se imprima un salto de línea doble
            print(f"{numero_linea:03d}: {contenido_linea}", end='')

# Si no se pasa el nombre del archivo, se muestra este error
except ValueError as error_argumento:
    print("Error:", error_argumento)

# Si el archivo no existe, se muestra este mensaje
except FileNotFoundError:
    print("Error: El archivo no se encontró.")

# Para cualquier otro tipo de error inesperado
except Exception as error_general:
    print("Ha ocurrido un error:", error_general)
