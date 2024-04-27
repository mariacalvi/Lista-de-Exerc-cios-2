def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"The file '{file_name}' has {num_lines} lines.")
    except FileNotFoundError:
        print("File not found. Please check the file nam.")

file_name = input("Enter the file name: ")


count_lines_in_file(file_name)
