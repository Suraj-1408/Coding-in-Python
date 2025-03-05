def alternate(lis):
    '''
    for i,value in enumerate(lis):
        print(value)
        i = i+1
    '''

    #note the simple increment statement DOESN;T AFFECT THE loop Structure. the for loop will follow next element sequentially without skipping the  next of element which was expected.

    #HENCe we need to make use of range in loop.
    
    for i in range(0,len(lis),2):
    #here third parameter is called step , used to step to certain index after each iteration is completed.
        print(lis[i])


lis = [1,2,3,4,5]
print("Given list:")
for i in lis:
    print(i)

print("ALternate elements in given list:")
alternate(lis)
