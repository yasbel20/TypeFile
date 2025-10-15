# Autor: Yasbel Soto
# Git: [Tu enlace de Git]

# Crear un programa que busca cuántas veces aparece un texto en un archivo
# Debemos crear un programa llamado FindText.py que reciba dos argumentos en la consola:

# Importamos los módulos
import os   # Interactúa con el sistema operativo, en este caso para limpiar la pantalla
import sys  # Permite trabajar con los argumentos pasados al script desde la línea de comando

# Para tener claro el orden de los argumentos pasados por consola
# sys.argv[0] → "FindText.py"
# sys.argv[1] → "documento.txt"
# sys.argv[2] → "Hola"

try:
    # Verificamos si se han pasado los argumentos correctos
    if len(sys.argv) < 3:
        raise ValueError("Falta el nombre del archivo o el texto a buscar.")
     
    # Inicializamos las variables con los argumentos pasados
    archivo = sys.argv[1]  # El nombre del archivo a leer
    texto = sys.argv[2]    # El texto que queremos buscar en el archivo

    # Limpiar pantalla antes de mostrar el resultado
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Leemos el archivo y contamos las coincidencias del texto
    with open(archivo, 'r', encoding="utf-8") as f:  # Abrimos el archivo en modo lectura, asegurando la correcta codificación
        contenido = f.read()  # Leemos todo el contenido del archivo y lo guardamos en la variable 'contenido'
        coincidencias = contenido.count(texto)  # Contamos cuántas veces aparece el texto en el archivo
        print(f"{texto} : {coincidencias}")  # Imprimimos el resultado: cuántas veces aparece el texto en el archivo

# Capturamos posibles errores y mostramos mensajes apropiados
except ValueError as ve:  # Si los argumentos son incorrectos o insuficientes, mostramos un error
    print(f"Error: {ve}")        
except FileNotFoundError:  # Si el archivo no se encuentra, indicamos que no existe
    print(f"El archivo '{archivo}' no existe.")
except Exception as e:  # Para cualquier otro error inesperado, mostramos un mensaje genérico
    print(f"Ocurrió un error al leer el archivo: {e}")