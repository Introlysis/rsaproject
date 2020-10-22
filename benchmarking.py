import timeit as t

x = 4519727393728283736271616283726293746382929173847

functions = [
    "hf.joeIsPrime({})".format(x)
    ]

for timedFunc in functions:
  setup = "import helperfunctions as hf"
  n = 100000

  print("Timing: " + timedFunc)
  print((t.timeit(timedFunc,setup,number=n))/n)