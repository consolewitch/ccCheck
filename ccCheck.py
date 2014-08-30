'''
Simple python script to validate 16 digit credit card numbers against
the Luhn algorithm

Alex Speaks
twitter:@logicalmethods
'''

ccString = str(input("Enter all but the last digit of the CC number ->"))
total = 0
temp = 0
for count in range (0,15):
	if (count+1) % 2 == 1:
		temp = int(ccString[count])*2
		if temp >= 10:
			total = total + temp - 9
		else:
			total = total + temp
	else:
		total = total + int(ccString[count])
print "last digit should be ",10-(total%10)

