# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def is_anagram1(string1, string2):
    # [assignment] Add your code here
    return sorted(string1) == sorted(string2)

print(is_anagram1("hello", "check"))

def is_anagram2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    return (list1 == list2)






def is_anagram1(string1, string2):
    # [assignment] Add your code here
    return sorted(string1) == sorted(string2)

print(is_anagram1("below", "elbow"))

def is_anagram2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    return (list1 == list2)


