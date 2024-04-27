import os

def delete_file(file_name):
    if not os.path.exists(file_name):
        print("File not found. Please enter a valid file name.")
        return
    
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")

file_name = input("Enter the file name to delete: ")

delete_file(file_name)
