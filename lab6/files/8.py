import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        try:
            with open(file_name, 'w') as file:
                file.write(f"Content for file {file_name}\n")
            print(f"File '{file_name}' successfully created.")
        except Exception as e:
            print(f"An error occurred while creating '{file_name}': {e}")

# Example usage:
generate_text_files()
