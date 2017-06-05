#Find the largest palindromic number product of two 3-digit numbers

def main():
    #step backwards through possibilities until a palindromic number is found
    max=0
    for i in range(999,99,-1):
        for j in range(i,99,-1): #avoid duplicates
            if isPalindromeBetter(i*j) and ((i*j)>max):
                max=(i*j)
    print(max)

def isPalindrome(numtotest):
    r=0 #store reversed number
    num=numtotest #store original number
    while (num>0): #while number has more than 1 digit
        r*=10
        r+=num%10 #add last digit to the reversed number
        num//=10 #divide by 10 (go to the next digit)
    if (r==numtotest): #if num is equal to its reverse its a palindrome
        return True
    return False

def isPalindromeBetter(numtotest):
    return str(numtotest)==str(numtotest)[::-1]

main()
