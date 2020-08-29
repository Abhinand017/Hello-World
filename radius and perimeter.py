from math import pi
radius = int(input())

def perim(k):
	#your code goes here
	x=2*pi*k
	return x

def area():
	#your code goes here
	y=pi*(radius *radius )
	return y
	
print("Perimeter:", round(perim(radius), 1))
print("Area:",round(area(), 2))