def count_lines(file_path):
    try:
        sum=0
       #return sum(1 for i in open(file_path, 'r'))
        for i in open(file_path,'r'):
            sum+=1
        return sum
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# Example usage:
file_path = 'myfile.txt'  # Replace with the actual path of your text file
lines_count = count_lines(file_path)

if lines_count != -1:
    print(f"The number of lines in the file '{file_path}' is: {lines_count}")
