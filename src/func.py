# Write a function is_even that will return true if the passed in number is even.
def is_even(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
while (True):
    num = input("Enter a number: ")
    # Print out "Even!" if the number is even. Otherwise print "Odd"
    print(is_even(num))

num = int(input("Enter a number: "))
# Print out "Even!" if the number is even. Otherwise print "Odd"
print("Even!") if num % 2 == 0 else print("Odd")
