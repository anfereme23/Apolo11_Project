from demo.utils.functions import read_yaml, get_random_number, gen_missions
import argparse
import os


print("*** Bienvenidos a Apolo 11 ***")

# Ruta dinamica
path_yaml = f"{os.getcwd()}/demo/config/configapp.yaml"
config = read_yaml(path_yaml)

# Crear objeto ArgumentParser
parser = argparse.ArgumentParser(
    description="Generador de números aleatorios en rango (archivos) y tiempo de ejecucion"
)
# Argumento inicial para generar archivos
parser.add_argument(
    "--inicial",
    type=int,
    default=config["random_number_files"]["inicial"],
    help="Limite inferior del rango",
)

# Argumento final para generar archivos
parser.add_argument(
    "--final",
    type=int,
    default=config["random_number_files"]["final"],
    help="Limite superior del rango",
)

# Argumento intervalo de tiempo de ciclo
parser.add_argument(
    "--second_interval",
    type=int,
    default=config["second_interval"],
    help="Tiempo de ejecucion",
)
# Analizar argumentos
args = parser.parse_args()

# Genera numero de archivos aleatorio
number_files = get_random_number(args.inicial, args.final)
print(f"Number of files: {number_files}")
gen_missions(number_files, args.second_interval, config)
