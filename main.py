import math
math.pi

subtotal = 0

sz=input ("Hello good sir, what size pizza would you like?")

if sz == "Large":
  print ("Ok that 6$")
  subtotal = subtotal + 6 
elif sz == "ExtraLarge":
  print ("Ok that will be 10$")
  subtotal = subtotal + 10
else:
  print ("I think im going to give you a large")
  subtotal = subtotal + 6

tp=input ("How many toppings would you like?")
if tp == "OneTop":
  print ('ok that will be 1$')
  subtotal = subtotal + 1
elif tp == "TwoTop":
  print ("ok that will be 1.75$")
  subtotal = subtotal + 1.75
elif tp == "ThreeTop":
  print ("Ok that will be 2.50$")
  subtotal = subtotal + 2.50
elif tp == "FourTop":
  print ("Ok that will be 3.35$")
  subtotal = subtotal + 3.35
else:
  print ("Im going to give you TwoTop")
  subtotal = subtotal + 1.75

HST = subtotal * 0.13
total = subtotal + HST
print ("The subtotal is", subtotal)
print ("HST is", HST)
print ("The total is", total)