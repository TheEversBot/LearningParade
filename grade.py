print 'Fredwaretek Grade Calculator'
print '---------------------------'
def computegrade():
    score=raw_input('Please enter a grade between 0.0 and 1.0\n')
    try:
        fscore=float(score)
        if fscore < 0 or fscore > 1:
         print 'Please enter a valid grade'
        elif fscore >= 0.9:
         print 'A'
        elif fscore >= 0.8:
         print 'B'
        elif fscore >= 0.7:
         print 'C'
        elif fscore >= 0.6:
         print 'D'
        elif fscore < 0.6:
         print 'F'
    except:
        print 'Please enter a valid number'
computegrade()
