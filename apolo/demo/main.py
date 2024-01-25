from services import functions

print("Bienvenidos a Apolo11")

mision_number = functions.get_random_number(1, 5)
number_files = functions.get_random_number(1, 100)
print(f"Number of files: {number_files}")
functions.gen_file_name(5, 2)
