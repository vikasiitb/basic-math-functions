
x = int(input("Enter first number"))
y = int(input("Enter second number"))

a = input("What kind of operation do you wish to perform?\n\
A) Addition\n\
B) Subtraction\n\
C) Multiplication\n\
D) Remainder\n\
")

if a in ['A', 'A)','(A)','A) Addition']:
	z = x + y
	print(z)
elif a in ['B','B)','(B)','B) Subtraction']:
	z = x - y
	print(z)
elif a in ['C','C)','(C)','C) Multiplication']:
	z = x * y
	print(z)
elif a in ['D','D)','(D)','D) Remainder']:
  z = x % y
  print (z)
