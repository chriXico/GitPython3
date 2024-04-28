import random

numbers = [1,2,3,4,5,6,7,8,9,10]

new_list = random.sample(numbers, len(numbers))

print("Original list : ", numbers)

print("List after shuffle", new_list)
