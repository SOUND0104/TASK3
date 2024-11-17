# QUESTION 1
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

#QUESTION 2
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]

prime_count = len(prime_numbers)

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", prime_count)

#QUESTION 3

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy_number(num):
    seen = set()  
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))  
    return num == 1
happy_numbers = [num for num in numbers if is_happy_number(num)]
happy_count = len(happy_numbers)

print("Happy Numbers:", happy_numbers)
print("Count of Happy Numbers:", happy_count)

#QUESTION 4
def sum_first_last_digit(number):
    num_str = str(number)
    last_digit = int(num_str[-1])
    return first_digit + last_digit
number = int(input("Enter an integer: "))
result = sum_first_last_digit(number)
print("Sum of the first and last digit:", result)

#QUESTION 5
def distribute_mangoes(mangoes, M):
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - M + 1):
        current_diff = mangoes[i + M - 1] - mangoes[i]
        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff

mangoes = [12, 7, 5, 9, 15, 3, 11]
M = 3
result = distribute_mangoes(mangoes, M)
print("Minimum difference between max and min mangoes:", result)

#QUESTION 6

list1 = [1, 2, 3, 4, 20]
list2 = [3, 4, 6, 1, 8]
list3 = [4, 2, 10, 3, 11]
merged_list = list1 + list2 + list3
duplicates = set()
seen = set()
for item in merged_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicates in the lists:", duplicates)

#QUESTION 7

def first_non_repeating(nums):
    counts = Counter(nums)
    for num in nums:
        if counts[num] == 1:
            return num
    return None 
nums = [4, 5, 1, 2, 1, 5, 4, 3]
result = first_non_repeating(nums)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There is no non-repeating element.")

#QUESTION 8
 def find_min(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return nums[0]  


nums = [6, 7, 9, 15, 19, 2, 3]
min_element = find_min(nums)
print(f"The minimum element in the rotated and sorted list is: {min_element}")


