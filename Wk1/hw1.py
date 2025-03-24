############################################################################
## Homework Assignment Week 1: Python Programming and Complexity Analysis
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Oct. 7, 2024
## Description: check the number that can be divided by prime numbers.
##              Then, that prime number is stored into a list. After loops,
##              returns all prime factors of an integer (increasing order).
############################################################################
import time

def factors(n):
    ans = []

    # Dividing by 2
    while n % 2 == 0:
        ans.append(2)
        n //= 2

    # Dividing by odd numbers
    d = 3
    while d <= int(n**(1/2))+1:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 2

    # if the number is left
    # that would be prime number
    if n > 1:
        ans.append(n)

    # Return an empty array
    # if there is only one prime number
    if len(ans) == 1:
        return []

    return ans

def measuring_time_factors(n_values):

    table = []
    for n in n_values:
        start = time.time()
        factors(n)
        end = time.time()
        table.append(end-start)

    return table

if __name__ == "__main__":
    print(factors(12))

    n_values = [1000000007, 10000000019, 100000000003, 1000000000039, 10000000000037,
                100000000000031,1000000000000037, 10000000000000061]
    time = measuring_time_factors(n_values)

    print("n\t\t\t\t\tT(n) (seconds)")
    for i in range(len(time)):
        print(f"{n_values[i]}\t\t{time[i]}")

