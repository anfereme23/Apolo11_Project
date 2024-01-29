import random
import hashlib
import os
import time
import yaml
import logging
from datetime import datetime
from yaml.loader import SafeLoader
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


def gen_hash(date: str, mission: str, device_type: str, device_status: str):
    hash_object = hashlib.sha256()
    concat = f"{date}{mission}{device_type}{device_status}"
    hash_object.update(concat.encode())
    result = hash_object.hexdigest()
    return result


def gen_file(file_name: str, content: Content):
    # Genera el content del archivo
    content_dict: Dict[str, any] = {
        "date": content.date,
        "mission": content.mission,
        "device_type": content.device_type,
        "device_status": content.device_status,
        "hash": content.hash,
    }
    # Crea un archivo con el nombre proporcionado
    with open(file_name, "w") as file:
        yaml.dump(content_dict, file)


def gen_folder(path: str, logger):
    try:
        # Crea una carpeta con el nombre proporcionado
        os.mkdir(path)

    except FileExistsError as e:
        logger.error("No se puede crear una carpeta existente")
    except Exception as e:
        logger.error(f"Error creando la carpeta: {e}")


def gen_missions(number_files: int, second_interval: int, config: dict):
    try:
        # Rutas dinamicas
        path = os.getcwd()
        path_devices = f"{path}/files/devices"
        path_reports = f"{path}/files/reports"
        path_backup = f"{path}files/backups"
        path_logs = f"{path}/files/logs"
        # Genera el achivo log
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
                date = datetime.now().strftime(config["file_date_format"])

                # Genera un numero aleatorio para los datos en el archivo de configuración
                random_mision_number = get_random_number(
                    config["random_number_missions"]["inicial"],
                    config["random_number_missions"]["final"],
                )
                random_device_type_number = get_random_number(
                    config["random_number_device_types"]["inicial"],
                    config["random_number_device_types"]["final"],
                )
                random_device_status_number = get_random_number(
                    config["random_number_device_status"]["inicial"],
                    config["random_number_device_status"]["final"],
                )

                # Obtiene los nombres de los datos segun el número aletorio
                mission_name = config["missions_name"].get(random_mision_number)
                device_status = config["device_status"].get(random_device_status_number)
                device_type = config["device_types"].get(random_device_type_number)

                # Genera el nombre del archivo
                mission = config["missions"].get(random_mision_number)
                file_name = f"APL-{mission}-{i}-{date}.log"
                # Genera la ruta del archivo dentro de ciclo
                file_path = os.path.join(path_ciclo, file_name)

                # Genera el content del archivo
                if mission_name != "Unknown":
                    content = Content(
                        date=date,
                        mission=mission_name,
                        device_type=device_type,
                        device_status=device_status,
                        hash=gen_hash(date, mission_name, device_type, device_status),
                    )
                else:
                    content = Content(
                        date=date,
                        mission=mission_name,
                        device_type="unknown",
                        device_status="unknown",
                    )

                # Crea el archivo
                gen_file(file_path, content)
                logger.info(f"Archivo '{file_name}' generado en '{file_path}'")

            # Incrementa el iterador del ciclo y ejecuta el siguiente en el intervalo de tiempo establecido
            ciclo += 1
            time.sleep(second_interval)

    except Exception as e:
        logger.error(f"Error creando la misión: {e}")
