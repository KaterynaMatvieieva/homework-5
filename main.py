# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# import random
#
# nums = []
# NUM_SIZE = 10
#
# for i in range(NUM_SIZE):
#     nums.append(random.randint(-50,50))
#
# print(nums)
#
# negative_sum = 0
# even_sum = 0
# odd_sum = 0
# product_index3 = 1
# product_min_max = 1
# sum_between_positive = 0
#
# for number in nums:
#     if number < 0:
#         negative_sum += number
#
#     if number % 2 == 0:
#         even_sum += number
#
#     if number % 2 != 0:
#         odd_sum += number
#
# min_nums_index = nums.index(min(nums))
# max_nums_index = nums.index(max(nums))
#
# if min_nums_index > max_nums_index:
#     min_nums_index, max_nums_index = max_nums_index, min_nums_index
#
# for i in range(min_nums_index + 1, max_nums_index):
#     product_min_max = product_min_max * nums[i]
#
# first_positive_index = 0
# last_positive_index = 0
#
# for i in range(len(nums)):
#     if nums[i] > 0:
#         first_positive_index = i
#         break
#
# for i in range(len(nums) - 1, -1, -1):
#     if nums[i] > 0:
#         last_positive_index = i
#         break
#
# for i in range(first_positive_index + 1, last_positive_index):
#     sum_between_positive += nums[i]
#
# for i in range(1,len(nums)):
#     if i % 3 == 0:
#         product_index3 = product_index3 * nums[i]
#
# print(f"Sum of negative values is : {negative_sum}, sum of even values is: {even_sum}, sum of odd values is {odd_sum}")
# print(f"Product of elements with /3 indexes is: {product_index3}, product of values between min amd max: {product_min_max}")
# print(f"Sum of values between the first and the last positive: {sum_between_positive}")


# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
#
# import random
#
# nums = []
# NUM_SIZE = 10
#
# for i in range(NUM_SIZE):
#     nums.append(random.randint(-50,50))
#
# print(nums)
#
# even_list = []
#
# for number in nums:
#     if number % 2 == 0:
#         even_list.append(number)
#
# print(f"Even_values: {even_list}")
#
# odd_list = []
#
# for number in nums:
#     if number % 2 != 0:
#         odd_list.append(number)
#
# print(f"Odd values: {odd_list}")
#
# negative_list = []
#
# for number in nums:
#     if number < 0:
#         negative_list.append(number)
#
# print(f"Negative values: {negative_list}")
#
# positive_list = []
#
# for number in nums:
#     if number > 0:
#         positive_list.append(number)
#
# print(f"Positive values: {positive_list}")
