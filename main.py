
from services import functions
print("Bienvenidos a Apolo11")

misiones = {
    1: "ORBONE",
    2: "CLNM:",
    3: "TMRS",
    4: "GALXONE",
    5: "UNKN"
    }

mision_number = functions.get_random_number(1,5)

mision_name = misiones.get(mision_number)
number_files = functions.get_random_number(1,100)
print(f"Mision: {mision_name}" )
print(f"Number of files: {number_files}" )
functions.gen_file_name(mision_name, 5, 2)
print("prueba github")