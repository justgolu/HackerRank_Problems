### Simple array sum
# Constrains: 
#   size of array greater than zero
#   each element must be less than 1000
###
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    for n in range(0,size):
        if size > 0:
            i = float(input("Enter the number:"))
            if i <= 1000:
                ar.append(i)
            else:
                return 'Invalid number'
        else: 
            return('Enter valid size')
    print(ar)
    m=0
    for _ in ar:
        
        m=m+_
    print(m)

        
size = int(input("Enter the size: "))
ar = []
simpleArraySum(ar)