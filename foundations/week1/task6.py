# Task 6. A palindrome is a word or phrase that reads the same forwards and backwards (e.g., "madam"). This program asks the user for a word and checks if the word is a palindrome. It does this by comparing the word with its reverse (word[::-1]). If they are the same, it informs the user that the word is a palindrome; otherwise, it says it is not.

x = input("enter a string: ")

if x == x[::-1]:
    print(f"The word '{x}' is a palindrome")
else:
    print(f"The word '{x}' is not a palindrome")

