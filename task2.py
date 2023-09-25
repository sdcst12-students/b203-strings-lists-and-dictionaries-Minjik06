#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    k=1
    for i in range(myNumber):
        if k !=0 and myNumber%k==0:
            factors.append(k)
            k+=1
        else:
            k+=1
    print(factors)



if __name__ == "__main__":
    main()