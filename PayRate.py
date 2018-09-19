print 'Welcome to Fredwaretek Pay Rate calculator\n'
print 'please follow the instructions now\n'
print '***********\n'
#Give employees 1.5 times the hourly rate for hours owrked above 40 hours
try:
    hours=input('Hours per week\n')
    rate=input('Pay Rate\n')    
    fhours=float(hours)
    frate=float(rate)
    if fhours < 40 :
        pay=fhours*frate
    elif hours == 40 :
        pay=fhours*frate
    elif fhours > 40 :
        pay=(fhours-40)*frate*1.5+(40*frate)
    text='Your pay rate is: $'
    print text,pay
    print 'COPYRIGHT FREDWARETEK. WE WILL SUE. WARNING WARNING.'

except:
     print 'Please, numerical input only'
