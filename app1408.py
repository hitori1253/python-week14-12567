#use of range()
def testRange(n):
    print('สูตรคูนแม่ ' +  str(n))
    values = range(1,12+1)
    #values = range(4)
    #iterate form i = 0 to i = 12
    for i in values:
        print("%d * %d = %d" %(n,i,n*i))