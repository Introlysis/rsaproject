import timeit as t

timedFunc = "hf.joeIsPrime(52957)"
setup = "import helperfunctions as hf"
n = 100000

print("Timing: " + timedFunc)
print((t.timeit(timedFunc,setup,number=n))/n)