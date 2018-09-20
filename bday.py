import datetime
print "   ________)"                                      
print "  (, /              /)                         /) "
print "    /___, __   _  _(/ _   _ _   __   _ _/_  _ (/_ "
print " ) /     / (__(/_(_(_ (_(/ (_(_/ (__(/_(___(/_/(__"
print "(_/                                               "
print "Chrono Remindulator"
age=input('Please enter the year you were born\n')
try:
	if age < 1900 or age > 2019:
		print 'valid year please'
	elif age > 1900 and age < 2019:
		now=datetime.datetime.now()
		math=age-now.year
		print math
except:
	print 'number please'