from django.test import TestCase

# Create your tests here.
def string_to_set(text):
    return set(text.replace(","," ").strip().split())
# text1 = "hello"
# text2 = "hello, buddy"
# text3 = "hello, I'm, here"

# set1 = string_to_set(text1)
# set2 = string_to_set(text2)
# set3 = string_to_set(text3)

# print(set1)  # Output: {'hello'}
# print(set2)  # Output: {'hello', 'buddy'}
# print(set3)  # Output: {'hello', "I'm", 'here'}
