# List Set, Dictionary
# my_char = [chat for param in iterable]
import char as char

# Set just replace {} instead of []
my_list = [char for char in 'vamsi']
print(my_list)

my_list_two = [num * 2 for num in range(1, 10)]
print(my_list_two)

my_list_three = [nums ** 2 for nums in range(1, 10) if nums % 2 != 0]
print(my_list_three)

simple_dictionary = {'a': 1, 'b': 2}
result_dictionary = {key: value * 2 for key, value in simple_dictionary.items()}
print(result_dictionary)

result_dictionary_One = {key: value ** 2 for key, value in simple_dictionary.items() if value % 2 == 0}
print(result_dictionary_One)

result_dictionary_two = {num: num * 2 for num in [1, 2, 3]}
print(result_dictionary_two)

some_list = ['b', 'a', 'd', 'e', 'a', 'e']
result_duplicate = list(set([x
                         for x in some_list if some_list.count(x) > 1]))
print(result_duplicate)
