"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def middle(list):
     list = sorted(list)
     mid = len(list)
     if mid%2 == 1:
         return list[mid//2]
     else:
         average = (list[mid//2]+list[(mid-1)//2])/2
         return average

    

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(middle(numbers))
