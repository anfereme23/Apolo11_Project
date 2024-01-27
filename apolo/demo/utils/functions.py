import random
import json
import os
import time
import yaml
import logging
from yaml.loader import SafeLoader
from demo.utils import functions
from demo.models.content import Content
from typing import Dict


def gen_logger(path_logs: str):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),  # Manejador para la consola
            logging.FileHandler(
                os.path.join(path_logs, "archivo_logs.log")
            ),  # Manejador para el archivo
        ],
    )
    return logging.getLogger(__name__)


def read_yaml(path: str) -> dict:
    """permite leer un archivo yaml y devolver el contenido como dict

    :param path: ruta archivo
    :type path: str
    :return: rdiccionario con los datos YAML, de lo contrario devuelve Ninguno
    :type: dict
    """
    content: dict = None
    try:
        with open(path) as file:
            content = yaml.load(file, Loader=SafeLoader)
    except Exception as ex:
        print(ex)
        content = None
    return content


def get_random_number(n1: int, n2: int) -> int:
    return random.randint(n1, n2)


def gen_file(file_name: str, content: Content):
    content_dict: Dict[str, any] = {
        "date": content.date,
        "device_status": content.device_status,
        "device_type": content.device_type,
        "hash": content.hash,
        "mission": content.mission,
    }
    # Crea un archivo con el nombre proporcionado
    with open(file_name, "w") as file:
        json.dump(content_dict, file)


def gen_folder(path: str, logger):
    try:
        # Crea una carpeta con el nombre proporcionado
        os.mkdir(path)

    except FileExistsError as e:
        logger.Error("No se puede crear una carpeta existente")
    except Exception as e:
        logger.Error(f"Error creando la carpeta: {e}")


def gen_missions(number_files: int, second_interval: int, config: str):
    try:
        # Rutas dinamicas
        path = os.getcwd()
        path_devices = f"{path}/files/devices"
        path_reports = f"{path}/files/reports"
        path_backup = f"{path}files/backup"
        path_logs = f"{path}/files/logs"
        logger = gen_logger(path_logs)

        ciclo = 1
        while True:
            # Genera una subcarpeta con el nombre del ciclo
            path_ciclo = f"{path_devices}/ciclo-00{ciclo}"
            gen_folder(path_ciclo, logger)
            # Genera el número de reportes por ciclo
            # TODO: cambiar 3 por el "number_files" (por ahora genera 2 archivos para probar)
            for i in range(1, 3):
                # Genera una fecha con el formato especificado en el archivo de configuración
                timestamp = time.strftime(config["file_date_format"])

                # Genera un número aleatoria entre 1 y 5 para el nombre de la mision
                mision_number = functions.get_random_number(1, 5)

                # Obtiene el nombre de la misión de acuerdo al número generado
                mision_name = config["missions"].get(mision_number)

                # Genera el nombre del archivo
                file_name = f"APL-{mision_name}-{i}-{timestamp}.log"
                file_path = os.path.join(path_ciclo, file_name)

                # Genera el content del archivo
                content = Content(
                    date="2024-01-26",
                    device_status="OK",
                    device_type="Tipo1",
                    hash=123456,
                    mission="Misión1",
                )
                # Crea el archivo
                gen_file(file_path, content)
                logger.info(f"Archivo '{file_name}' generado en '{file_path}'")

            # Incrementa el iterador del ciclo y ejecuta el siguiente en el intervalo de tiempo establecido
            ciclo += 1
            time.sleep(second_interval)

    except Exception as e:
        logger.info(f"Error creando la misión: {e}")
