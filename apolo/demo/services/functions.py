import random
import os
import time
from services import functions


def get_random_number(n1: int, n2: int) -> int:
    return random.randint(n1, n2)


def gen_file(file_name: str, content: str = "Estoy monitoreando"):
    # Crea un archivo con el nombre proporcionado
    with open(file_name, "w") as archivo:
        archivo.write(content)


def gen_file_name(
    time_interval: int,
    number_files: int,
    directory: str = "devices",
):
    try:
        misiones = {1: "ORBONE", 2: "CLNM", 3: "TMRS", 4: "GALXONE", 5: "UNKN"}
        parent_dir = "./"
        path = os.path.join(parent_dir, directory)

        # Verifica si el directorio existe, si no, lo crea
        if not os.path.exists(path):
            os.mkdir(path)

        i = 1
        while i <= number_files:
            # timestamp = time.strftime("%Y%m%d%H%M%S")
            # Genera un número aleatoria entre 1 y 5
            mision_number = functions.get_random_number(1, 5)
            # Obtiene el nombre de la misión de acuerdo al número generado
            mision_name = misiones.get(mision_number)
            # Genera el nombre del archivo
            file_name = f"APL-{mision_name}-{i}.log"
            file_path = os.path.join(path, file_name)
            gen_file(file_path)
            print(f"Archivo '{file_name}' generado en '{path}'")
            time.sleep(time_interval)
            i += 1
    except FileExistsError as e:
        print("No se puede crear una carpeta existente")
    except Exception as e:
        print(f"Error creando la carpeta: {e}")
