

def Native_search(l,target,high,low ):
    if high == None:
           high = len(l)-1

    if low == None:
        low = 0

    if high < low:
        return -1 





def bin_search(l,target,low = None,high = None):
    midpoint = len(l)//2 


    if l[midpoint] == target:
        return midpoint

    elif l[midpoint] > target:
        return bin_search(l,target,low,midpoint-1)

    else :
        return bin_search(l,target,midpoint-1,high)




x = list(range(100))

print(bin_search(x,57))