def addition():
	print("Addition")
	n = float(input("enter the number:"))
	t = 0 #total number enter
	ans = 0
	while n !=0:
		ans = ans + n
		t+=1
		n = float(input("enter another number (0 to calculate): "))
	return [ans,t]
def subtraction ():
	print("Subtraction");
	n = float(input("enter the number: "))
	t = 0 #Total number enter
	sum = 0
	while n != 0:
		ans = ans - n
		t+=1
		n = float(input("enter another number to (0 to calculate): "))
	return [ans,t]
def multiplication ():
	print("Multiplication")
	n = float(input("Enter the number: "))
	t = 0 #Total number enter
	ans = 1
	while n != 0:
		ans = ans*n
		t+= 1
		n = float(input("enter another number (0 to calculate): "))
	return [ans,t]
def average():
	an =[]
	an = addition()
	t = an[1]
	a = an[0]
	ans = a/t
	return [ans,t]
 #main
while True:
	list = []
	print("my first python program!")
	print("simple Calculator in python by Anubhav Sharma")
	print("enter 'a' for addition")
	print("enter 's' for substraction")
	print("enter 'm' for multiplication")
	print("enter 'v' for average")
	print("enter 'q' for quit")
	c = input(" ")
	if c != 'q':
		if c == 'a':
			list = addition()
			print("Ans = ", list[0], " total inputs ", list[1])
		elif c== 's':
			list = subtraction()
			print("Ans = ", list[0], " total inputs ", list[1])
		elif c == 'm':
			list = multiplication()
			print("Ans = ", list[0], " total inputs ", list[1])
		elif c =='v':
			print("Ans = ", list[0], " total inputs ", list[1])
		else:
			print("Sorry, invalid character")
	else:
		break


































