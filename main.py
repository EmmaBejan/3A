import math
math.pi

HST = 1.13
Large = 6.00
ExtraLarge = 10.00
OneTop = 1.00
TwoTop = 1.75
ThreeTop = 2.50
FourTop = 3.35
sz=input ("Hello good sir, what size pizza would you like?")

if Large > ExtraLarge:
  print ("Ok that will be 6$")
if ExtraLarge > Large:
  print ("Ok that will be 10$")

tp=input ("How many toppings would you like?")

if OneTop > TwoTop:
  print ("Ok that will be 1$")
