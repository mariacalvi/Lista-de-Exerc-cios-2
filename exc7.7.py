import os

def create_directory_and_file(directory_name, file_name):
    try:

        if not os.path.exists(directory_name):
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' sucessfully created.")


        file_path = os.path.join(directory_name, file_name)
        with open(file_path, 'w') as file:
            file.write("File content temp.txt")

        print(f" '{file_name}' sucessfully created inside the directory'{directory_name}'.")
    except OSError as e:
        print(f"Error creating the directory or file: {e}")

directory_name = "temp"
file_name = "temp.txt"

create_directory_and_file(directory_name, file_name)
