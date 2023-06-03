import sys

# palindrome function 
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False 
    

# parity checker function
def parity_checker(n):
    if '.' in n:
        return 'no parity'
    else:
        num = int(n)
        if num % 2 == 0:
            return 'even parity'
        else:
            return 'odd parity'
        
num_oddparity = 0
num_evenparity = 0
num_noparity = 0
num_palindrome = 0
num_nopalindrome = 0


sys.stdin = open("input.txt",'r') 
sys.stdout = open("output.txt",'w') 
for i in range(5):
    string = input()
    new_string = string.split(' ') 
    
    # Count code
    if is_palindrome(new_string[1]) == True:
        num_palindrome += 1
    else:
        num_nopalindrome += 1
        
    if parity_checker(new_string[0]) == 'even parity':
        num_evenparity += 1
    elif parity_checker(new_string[0]) == 'odd parity':
        num_oddparity += 1
    else:
        num_noparity += 1
    
    # Output code    
    if is_palindrome(new_string[1]) == True:
        print(f'{new_string[0]} has a {parity_checker(new_string[0])} and {new_string[1]} is a palindrome')
    
    else:
        print(f'{new_string[0]} has a {parity_checker(new_string[0])} and {new_string[1]} is not a palindrome')



sys.stdout = open("record.txt",'w') 

per_odd = int((num_oddparity/5)*100)
per_even = int((num_evenparity/5)*100)
per_noparity = int((num_noparity/5)*100)
per_palin = int((num_palindrome/5)*100)
per_nopalin = int((num_nopalindrome/5)*100)

print(f'Percentage of odd parity: {per_odd}% \nPercentage of even parity: {per_even}% \nPercentage of no parity: {per_noparity}% \nPercentage of palindrome: {per_palin}% \nPercentage of non-palindrome: {per_nopalin}%')
