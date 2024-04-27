def display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

file_name = input("Enter the file name: ")

display_file_content(file_name)
