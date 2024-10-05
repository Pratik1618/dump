num = int(input("Enter a number: "))
def armstrong(a):
    b = a
    arm = 0
    while a != 0:
        n = a % 10
        arm = arm + (n * n * n)
        a = a // 10
    if arm == b:
        print("The number is Armstrong")
    else:
        print("The number is not an Armstrong")
def palindrome(c):
    d = c
    pall = 0
    while c != 0:
        m = c % 10
        pall = (pall * 10) + m
        c = c // 10
    if pall == d:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
armstrong(num)
palindrome(num)
