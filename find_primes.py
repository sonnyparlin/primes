from cmd import Cmd
import random
import time
import ast
import operator as op


class MyPrompt(Cmd):
    prompt = 'findPrimes> '
    intro = "Welcome! Type in a number to see if it's prime. Type q to quit"
    
    __hidden_methods = ('do_EOF','emptyline','is_prime','is_valid', 'rabinMiller')    
    def get_names(self):
        return [n for n in dir(self.__class__) if n not in self.__hidden_methods]
     
    def do_exit(self, inp):
        '''exit the application. Shorthand: x q Ctrl-D.'''
        print("Bye")
        return True
        
    do_EOF = do_exit
        
    def emptyline(self):
        pass
    
    # found this function on https://inventwithpython.com/rabinMiller.py
    def rabinMiller(self, num):
        # Returns True if num is a prime number.

        s = num - 1
        t = 0
        while s % 2 == 0:
            # keep halving s while it is even (and use t
            # to count how many times we halve s)
            s = s // 2
            t += 1

        for trials in range(5): # try to falsify num's primality 5 times
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1: # this test does not apply if v is 1.
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
        return True

    # found this function on https://inventwithpython.com/rabinMiller.py
    def is_prime(self, num):
        # Return True if num is a prime number. This function does a quicker
        # prime number check before calling rabinMiller().

        if (num < 2):
            return False # 0, 1, and negative numbers are not prime

        # About 1/3 of the time we can quickly determine if num is not prime
        # by dividing by the first few dozen prime numbers. This is quicker
        # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
        # prove that a number is prime.
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        if num in lowPrimes:
            return True

        # See if any of the low prime numbers can divide num
        for prime in lowPrimes:
            if (num % prime == 0):
                return False

        # If all else fails, call rabinMiller() to determine if num is a prime.
        return self.rabinMiller(num)

    def eval_(self, node):
        global operators
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return operators[type(node.op)](self.eval_(node.left), self.eval_(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return operators[type(node.op)](self.eval_(node.operand))
        else:
            raise ValueError(node)

    def eval_expr(self, expr):
        return self.eval_(ast.parse(expr, mode='eval').body)
        
    def is_valid(self, n):        
        if not n:
            return False
        
        try:
            n = int(self.eval_expr(n))
        except ValueError:
            print("couldn't convert to int")
            return False
        
        if n < 1:
            return False
    
        return n
    
    def default(self, inp):
        if inp.strip() == 'q':
            return self.do_exit(inp)
        
        # Let's not crash ourselves.    
        if '**' in inp:
            a = inp.split("**")
            if len(a[1]) > 6:
                print("Bro, I'm a computer not a rocket ship... the fuck outta here with {}".format(inp))
                return

        n = self.is_valid(inp)
        if not n:
            print("Please enter a valid number")
        else:
            start = time.time()
            if inp != str(n):
                print("Expanded expression to {} decimals".format(len(str(n))))
            sys.stdout.write("{}\n".format(self.is_prime(n)))
            end = time.time()
            print("found in {:.9f} seconds".format(end - start))

if __name__ == '__main__':
    import sys
    inner_loop_iterations = 0
    # supported operators
    operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                 ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
                 ast.USub: op.neg}
    MyPrompt().cmdloop()
