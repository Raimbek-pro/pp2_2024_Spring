def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage:
input_string = "Hello World"

result = count_upper_lower(input_string)

print(f"Number of upper case letters: {result[0]}")
print(f"Number of lower case letters: {result[1]}")
