import os

def check_access(path):
    # Check existence
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        # Check readability
        if os.access(path, os.R_OK):
            print(f"Path '{path}' is readable.")
        else:
            print(f"Path '{path}' is not readable.")

        # Check writability
        if os.access(path, os.W_OK):
            print(f"Path '{path}' is writable.")
        else:
            print(f"Path '{path}' is not writable.")

        # Check executability
        if os.access(path, os.X_OK):
            print(f"Path '{path}' is executable.")
        else:
            print(f"Path '{path}' is not executable.")
    else:
        print(f"Path '{path}' does not exist.")


specified_path = input("Enter the path: ")
check_access(specified_path)
