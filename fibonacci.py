n = int(input("Enter the number of terms : "))
n1 = 0
n2 = 1
count = 0
if n < 0:
    print("Invalid term...!!\n")
elif n == 1:
    print("Fibonacci sequence for given ", n, "term is :\n")
    print(n1)
else:
    print("Fibonacci sequence for given ", n, "term is :\n")
    while count < n:
        print(n1)
        nth = n1 + n2
        # update the next values of n1 and n2
        n1 = n2
        n2 = nth
        count += 1
