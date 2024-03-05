#!/usr/bin/python3

# Create a function to calculate the percentage of a number and return it.
#
# Create a function that takes in a list and returns the last item in the list
#
# Create a function that takes in a dictionary and returns the value of the second item
#
# Create a function that adds two lists together and returns the value


numerator_insert = int(input("Insert numerator: "))

denominator_insert = int(input("Insert denominator: "))

def calculate_percentage( numerator_insert, denominator_insert):
  if denominator_insert == 0:
    raise ZeroDivisionError("Cannot calculate percentage with a zero denominator.")

  return (numerator_insert / denominator_insert ) *100


percentage = calculate_percentage (numerator_insert, denominator_insert)
print(f"{percentage:.2f}%")






"""
 This function calculates the percentage of a numerator relative to a denominator.

 Args:
     numerator: The value to be expressed as a percentage.
     denominator: The total value against which the percentage is calculated.

 Returns:
     The percentage value as a float.
 """