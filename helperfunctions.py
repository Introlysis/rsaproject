#Euclid's stuff
def joeGCD(a,b):
  
    #handle negative a or b
    a = -a if a < 0 else a
    b = -b if b < 0 else b
  
    #we want a > b
    if b > a:
        temp = a
        a = b
        b = temp
    
    if b == 0 and a == 0:
        print("0 or Undefined, depending on who you ask")
        return
  
    return joeGCD(b, a % b) if b>0 else a
    
  
def joeExtendedGCD(a, b):
  
    #handle negative a and/or b
    a = -a if a < 0 else a
    b = -b if b < 0 else b
  
    #we want a > b
    if b > a:
        temp = a
        a = b
        b = temp
    
    if b == 0 and a == 0:
        print("0 or Undefined, depending on who you ask")
        return
    
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = joeExtendedGCD(b, a % b)
        x = q
        y = p - q * (a // b)

    #assert bezout identity
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
  
    #GCD and bezout coefficients
    return (d, x, y)
    

#Primality and factoring
def joeIsPrime(x):
  
    if x == 2 or x == 3:
        return True
    
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    
    y = 5
    z = 7
    #count = 0
    
    while z <= (int(x**0.5) + 1):
        if x % z == 0 or x % y == 0:
            return False
        y = y + 6
        z = z + 6
        #count += 1
    #print(y,z,count)    
    return True
    
  
def joeFactorRSA(x):
#massively limited

    if x%2==0:
        print("2, "+str(x/2))
    for i in range(3,int(x**0.5),2):
        if x%i==0:
            print(str(i)+", "+str(x/i))
          

#Math helpers
def joeLCM(a,b):

    if a>b:
        return (a*b)//joeGCD(a,b)
    else:
        return (a*b)//joeGCD(b,a)