#Input Specification - An integer N, the number of terms to generate. Assume N >= 1.
#Output Specification - Print a list containing the first N terms of the Fibonacci sequence. The sequence starts with 0 and 1.
#Fibonacci: n = (n-1) + (n-2). Example: 0, 1, 1, 2, 3, 5, 8...

def ini_fibo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0, 1]

def fibo(n):
    count = n
    while count > 1:
        return (count-1) + (count-2)
    count -= 1

ni = input()
print(ini_fibo, fibo)
