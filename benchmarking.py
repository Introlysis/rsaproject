import timeit as t

x = 52957

functions = [
    "hf.joeIsPrime({})".format(x),
    "hf.benchIsPrime({})".format(x)
    ]

for timedFunc in functions:
  setup = "import helperfunctions as hf"
  n = 100000

  print("Timing: " + timedFunc)
  print((t.timeit(timedFunc,setup,number=n))/n)