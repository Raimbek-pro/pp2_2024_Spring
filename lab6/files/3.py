import os
#/Users/raiymbekomarov/Documents
def list_all(path):
    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)


specified_path = input("Enter the path: ")

if os.path.exists(specified_path):
    list_all(specified_path)
else:
    print("Invalid path. Please provide a valid path.")

