import os
import shutil

def delete_directory_with_contents(directory_name):
    try:
        if os.path.exists(directory_name):
            shutil.rmtree(directory_name)
            print(f"Directory '{directory_name}' and its contents deleted successfully.")
        else:
            print(f"Directory '{directory_name}' not found.")
    except OSError as e:
        print(f"Error deleting directory: {e}")

directory_name = "temp"
delete_directory_with_contents(directory_name)
