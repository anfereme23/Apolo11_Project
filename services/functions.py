import random
import os
import time

def get_random_number(n1: int, n2: int) -> int:
    return random.randint(n1, n2)

def gen_file(file_name: str, content: str = "Estoy monitoreando"):
    # Crea un archivo con el nombre proporcionado
    with open(file_name, 'w') as archivo:
        archivo.write(content)

def gen_file_name(mision: str, time_interval: int, number_files: int, directory: str = "devices"):
    try:
        parent_dir = "./"
        path = os.path.join(parent_dir, directory)

        # Verifica si el directorio existe, si no, lo crea
        if not os.path.exists(path):
            os.mkdir(path)

        i = 1
        while i <= number_files:
            #timestamp = time.strftime("%Y%m%d%H%M%S")
            file_name = f"APL-{mision}-{i}.log"
            file_path = os.path.join(path, file_name)
            gen_file(file_path)
            print(f"Archivo '{file_name}' generado en '{path}'")
            time.sleep(time_interval)
            i += 1
    except FileExistsError as e:
        print("No se puede crear una carpeta existente")
    except Exception as e:
        print(f"Error creando la carpeta: {e}")