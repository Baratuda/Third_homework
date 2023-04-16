import random as ra
print("Please input array size:")
array_length = int(input())
print("Please enter the number you want to calculate in the array.")
number = int(input())

array = [ra.randrange(1,10) for _ in range(array_length)]
dictionary= { i:abs(i-number) for i in array }
result = sorted(dictionary, key=dictionary.get)[0]

print(f"The nearliest number with inputed number in array {array} is {result}")