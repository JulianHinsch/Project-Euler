from math import sqrt

#gets all factors of a number (in this case 600,851,475,143)
#tests which ones are prime
#selects the maximum prime
def main():
    num=600851475143
    factors=getFactors(num)
    max=2
    for i in range(0,len(factors)):
        if factors[i]>max and isPrime(factors[i]):
            max=factors[i]
    print(max)

#tests if a number is prime
#brute force
def isPrime(num):
    for i in range(2,int(num)):
        if num%i==0:
            return False
    return True

#gets all factors of a given number
#somewhat efficient, only iterates to square root
def getFactors(num):
    factors=[]
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            factors.append(i)
            factors.append(num/i)
    return factors


main()
