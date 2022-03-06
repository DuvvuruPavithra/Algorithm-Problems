def anagram_check(str1,str2):
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == "__main__":

    str1 = input("Enter the String1: ")
    str2 = input("Enter the String2: ")
anagram_check(str1,str2)
