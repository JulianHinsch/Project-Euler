#sums all even fibonacci numbers below 4,000,000
#brute force
def main():
    first=1
    second=2
    third=0
    numsum=second
    while third<4000000:
        third=first+second
        if third%2==0:
            numsum+=third
        first=second
        second=third
    print(numsum)
    
main()
