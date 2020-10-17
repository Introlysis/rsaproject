import timeit as t

timedFunc = "hf.joeIsPrime(52957)"
setup = "import helperfunctions as hf"
n = 100000

#print(hf.joeGCD(52957,99689))
print((t.timeit(timedFunc,setup,number=n))/n)