import re

def camel_to_snake_case(camel_case_string):
    # Using regex to find and replace camel case with snake case
    snake_case_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case_string)
    return snake_case_string.lower()

# Example usage
camel_case_string = "camelCaseExample"
snake_case_result = camel_to_snake_case(camel_case_string)

print("Camel Case String:", camel_case_string)
print("Snake Case Result:", snake_case_result)
