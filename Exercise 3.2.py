"""
Add an 'except' in case of error
"""

try:
	h = raw_input("Enter Hours:")
	hrs = float(h)
	
	rate = raw_input("Enter Rate per Hour:")
	rp_hour = float(rate)

except:
	print "Error, please enter numeric input"
	quit() 

print "Rate per Hour:" 
print rp_hour
print "Hours:" 
print hrs 

if hrs <= 40:
	total_pay = rp_hour

else:
	total_pay = hrs * rp_hour + ((hrs-40) * rp_hour * 1.5)

print "Total Pay:"
print total_pay
