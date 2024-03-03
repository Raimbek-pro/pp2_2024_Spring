def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'output_file.txt'  # Replace with the desired output file path
my_list = [1, 2, 'three', 4.5, 'five']

write_list_to_file(file_path, my_list)
