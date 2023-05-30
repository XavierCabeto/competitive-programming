def is_palindrome(str, l, r):
    if str == None or l < 0 or r < 0:
      return False
    
    if l >= r:
      return True
    
    if str[l] == str[r]:
      return is_palindrome(str, l+1, r-1)
    
    return False

str = "abbba"

if(is_palindrome(str, 0, len(str)-1)):
  print(str, "is palindrome")
else:
  print(str, "is not palindrome")