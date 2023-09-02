def is_palindrome(word):
    def reverse(s):
        return s[::-1]

    rev = reverse(word)
    return word == rev


s = input("Enter a word: ")

if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
