def copy_file_with_extension_change(original_file, new_extension):
    try:
        with open(original_file, 'rb') as infile:
            content = infile.read()

        new_file_name = original_file.rsplit('.', 1)[0] + '.' + new_extension

        with open(new_file_name, 'wb') as outfile:
            outfile.write(content)

        print(f"File '{original_file}' copied to '{new_file_name}' with extension changed to '.{new_extension}'.")
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")

file_name = input("Enter the file name to copy: ")

copy_file_with_extension_change(file_name, 'copy')