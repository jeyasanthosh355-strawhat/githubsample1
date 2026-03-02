def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    # Compare original and reversed string
    return string == string[::-1]

# Input from user
text = input("Enter a string: ")

# Check palindrome
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
