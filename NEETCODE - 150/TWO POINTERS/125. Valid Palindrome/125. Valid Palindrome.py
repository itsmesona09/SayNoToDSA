import re
class Palindrome:
    def valid_palindrome(self, s):
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        return s[::-1] == s
        
palindome = Palindrome()
s = "A man, a plan, a canal: Panama"
print(palindome.valid_palindrome(s))