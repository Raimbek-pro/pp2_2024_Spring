import re

def split_string_at_uppercase(input_string):
    # Using regex to split the string at uppercase letters
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result

# Example usage
input_string = "SplitThisStringAtUpperCase"
result = split_string_at_uppercase(input_string)

print("Original String:", input_string)
print("Split Result:", result)
