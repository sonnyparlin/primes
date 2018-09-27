import sys

inner_loop_iterations: int = 0
n=1


def is_prime(n):
    a: int = 2
    global inner_loop_iterations

    if n == 1:
        return("Not prime")
    elif n == 2:
        return("Prime")

    while a * a <= n + 1:
        inner_loop_iterations += 1
        # This if statement reduces the number of inner loop iterations by roughy 50%
        # just weeding out the even numbers.
        if a % 2 == 0:
            a += 1
        else:
            a += 2

        if n % 2 == 0 or n % a == 0:
            return ("Not prime")
    else:
        if a > 2:
            return ("Prime")


while n != 0:
    sys.stdout.write("Enter a number to see if it's a prime number: ")
    n = input()
    if not n:
        continue
    if n == 'q':
        break
        
    try:
        n = int(n)
    except ValueError:
        print("Please enter a valid number")

    sys.stdout.write("{}\n".format(is_prime(n)))
    sys.stderr.write("Inner loops: {}\n\n".format(inner_loop_iterations))
    inner_loop_iterations=0