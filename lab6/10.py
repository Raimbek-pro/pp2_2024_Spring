import os

def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Check if the user has write access to the file
            if os.access(file_path, os.W_OK):
                # Delete the file
                os.remove(file_path)
                print(f"File '{file_path}' successfully deleted.")
            else:
                print(f"Error: No write access to file '{file_path}'. Cannot delete.")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_to_delete = 'C.txt'  

delete_file(file_to_delete)
