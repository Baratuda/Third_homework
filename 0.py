import random as ra
print("Please input array size:")
array_length = int(input())
print("Please enter the number you want to calculate in the array.")
number = int(input())

array = [ra.randrange(1,10) for _ in range(array_length)]
count = sum([i==number for i in array])  

print(f"count of number({number}) in array: {array} = {count}")