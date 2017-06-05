#brute-forcey - could be worse if incremented by 1 but still very inefficient

def main():
    i=20
    while not isValid(i):
        i+=20
    print(i)

def isValid(n):
    for j in range(2,21):
        if (n%j!=0):
            return False
    return True
    
main()
