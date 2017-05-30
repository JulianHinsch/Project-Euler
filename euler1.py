#sums all multiples of 3 or 5 under 1000
#doesn't add duplicates (i.e. 15 is only added once)
#brute force
def main():
    numsum=0
    for i in range(0,1000,1):
        if i%3==0 or i%5==0:
            numsum+=i
    print(numsum)
    
main()

