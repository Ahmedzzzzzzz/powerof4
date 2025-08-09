# Program to send if the number is power of 8 or not

# Take input
n = int(input("enter your number: "))

def checkifpower(n):
    # If n is less than equal to 0 just say no
    if(n <= 0):
        return False
    # If we reach lowest power of n return true
    if(n == 1):
        return True
    if (n%8 == 0):
        return checkifpower(n / 8)
    return False

if(checkifpower(n)):
    print("Power of 8")
else:
    print("Not power of 8")
