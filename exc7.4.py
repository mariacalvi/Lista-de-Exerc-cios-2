import os

def rename_file(original_file):
    if not os.path.exists(original_file):
        print("File not found. Please try again with a valid file name.")
        return
    
    file_name, file_extension = os.path.splitext(original_file)
    new_file_name = file_name + "_renamed" + file_extension

    try:
        os.rename(original_file, new_file_name)
        print(f"File renamed to '{new_file_name}'.")
    except OSError as e:
        print(f"Error renaming file: {e}")

file_name = input("Enter the file name to rename: ")

rename_file(file_name)
