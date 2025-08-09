# Program to send if the number is power of 4 or not

# Take input
n = int(input("enter your number: "))

def checkifpower(n):
    # If n is less than equal to 0 just say no
    if(n <= 0):
        return False
    # If we reach lowest power of n return true
    if(n == 1):
        return True
    if (n%4 == 0):
        return checkifpower(n / 4)
    return False

if(checkifpower(n)):
    print("Power of 4")
else:
    print("Not power of 4")