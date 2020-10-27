import timeit as t

x = 1000000

functions = [
    "hf.joeSetOfPrimesNaive({})".format(x),
    "hf.joeSieve({})".format(x)
    ]

for timedFunc in functions:
  setup = "import helperfunctions as hf"
  n = 1

  print("Timing: " + timedFunc)
  print((t.timeit(timedFunc,setup,number=n))/n)