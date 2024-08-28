def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring without the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
my_string = input("Enter a string: ")
if is_palindrome(my_string):
    print(f"'{my_string}' is a palindrome.")
else:
    print(f"'{my_string}' is not a palindrome.")
