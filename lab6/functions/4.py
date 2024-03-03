import time
import math

def delayed_square_root(value, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds for time.sleep()
    result = math.sqrt(value)
    print(f"Square root of {value} after {delay_ms} milliseconds is {result}")

# Example usage with the provided sample input:
input_value = 25100
delay_duration = 2123

print(f"Invoking square root function after {delay_duration} milliseconds for the value {input_value}...\n")
delayed_square_root(input_value, delay_duration)
