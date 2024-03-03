def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"File '{source_path}' successfully copied to '{destination_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_file_path = 'A.txt' 
destination_file_path = 'B.txt' 

copy_file(source_file_path, destination_file_path)
