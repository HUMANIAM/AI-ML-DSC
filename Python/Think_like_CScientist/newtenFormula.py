"""
newten formula used to find the square root of number. by assume the solution and then enhance
it repeatly till reach a solution that is close to the correct one.
"""
n = 16
approx = n/2
threshold = 0.01
better = 0
while True :
	better = (approx + n/approx)/2
	if abs(better - approx) < threshold :
		break
	approx = better

print("sqrt(%d) = %d" % (n, better))