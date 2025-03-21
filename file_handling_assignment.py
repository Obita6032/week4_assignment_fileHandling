def process_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename: The name of the input file.
        output_filename: The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Example: Modify each line by converting it to uppercase
                modified_line = line.upper()
                outfile.write(modified_line)
        print(f"File '{input_filename}' processed and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    process_file(input_filename, output_filename)