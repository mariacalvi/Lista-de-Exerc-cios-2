def invert_lines_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        inverted_lines = [line.strip()[::-1] + '\n' for line in lines]

        with open(output_file, 'w') as outfile:
            outfile.writelines(inverted_lines)

        print(f"Content of '{input_file}' inverted and saved to '{output_file}'.")
    except FileNotFoundError:
        print("File not found. Please try again.")


input_file = input("Enter file name: ")
output_file = input("Enter file name for inverted content: ")

invert_lines_in_file(input_file, output_file)
