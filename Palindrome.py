def is_palindrome(string):
    string=str(string)
    return string==string[::-1]

a=input("enter a string:")

if is_palindrome(a):
    print("palindrome")
else:
    print("not palindrome")