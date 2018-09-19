print 'Fredwaretek C to F converter 2\n'
print '--------\n'

inp=raw_input('Please enter a temperature in C\n')
name=raw_input('Please enter your name\n')

try:
    ftemp=float(inp)
    cel=(ftemp*1.8)+32
    text=' degrees farenheiht. Thanks'
    print cel,text,name
except:
    print 'please enter a number'
print '--------\n'
print 'Copyright Fredaretek WE WILL SUE.'
