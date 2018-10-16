# primes
Prime number finder in Python, uses Miller-Rabin algorithm.

## Examples
```python
findPrimes> 2**9941-1
Expanded expression to 2993 decimals
True
found in 11.142532110 seconds
findPrimes>
```

```python
findPrimes> 1000000007
True
found in 0.000202894 seconds
findPrimes> 
```

```
findPrimes> 2**11213-1
Bro, I'm a computer not a rocket ship... the fuck outta here with 2**11213-1
```
As you can see there's a restriction on the number of digits we can square. 
Feel free to lift the limit by commenting out or deleting the following code in the default function, or change the 6 to whatever:

```
# Let's not crash ourselves.    
if '**' in inp:
    a = inp.split("**")
    if len(a[1]) > 6:
        print("Bro, I'm a mac not a rocket ship... the fuck outta here with {}".format(inp))
        return
```
