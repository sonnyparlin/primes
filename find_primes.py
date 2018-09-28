from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'findPrimes> '
    intro = "Welcome! Type q to quit"
    
    __hidden_methods = ('do_EOF','emptyline','is_prime','is_valid')    
    def get_names(self):
        return [n for n in dir(self.__class__) if n not in self.__hidden_methods]
     
    def do_exit(self, inp):
        '''exit the application. Shorthand: x q Ctrl-D.'''
        print("Bye")
        return True
        
    do_EOF = do_exit
        
    def emptyline(self):
        pass
    
    def is_prime(self, n):
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
            return ("Prime")
        
    def is_valid(self, n):        
        if not n:
            return False
        
        try:
            n = int(n)
        except ValueError:
            return False
        
        if n < 1:
            return False
    
        return n
    
    def default(self, inp):
        if inp.strip() == 'q':
            return self.do_exit(inp)

        global inner_loop_iterations
        n = self.is_valid(inp)
        if not n:
            print("Please enter a valid number")
        else:
            sys.stdout.write("{}\n".format(self.is_prime(n)))
            sys.stderr.write("Inner loops: {}\n\n".format(inner_loop_iterations))
            inner_loop_iterations=0

if __name__ == '__main__':
    import sys
    inner_loop_iterations = 0
    MyPrompt().cmdloop()