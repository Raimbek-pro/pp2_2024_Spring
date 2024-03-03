import os

def analyze_path(path):
    # Check if the path exists
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        # Get the filename and directory portion
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path '{path}' does not exist.")

specified_path = input("Enter the path: ")
analyze_path(specified_path)
