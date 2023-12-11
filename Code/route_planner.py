#You will be given a list of integers, 
# they will be the height of a peak from ground level (1 = 100m). 
# #The peaks will appear in a single line as you travel from point A to B. 
#Rules:
#•	You don’t have to climb every peak. But you want to climb as many peaks as possible
#•	You only want to increase your altitude as going up and down would be too exhaustive. 
#•	There is no going backwards.

#There can be more than one possible output.

def peak(l):
    unique = set(l)
    list_2 = list(unique)
    list_2.sort()
    return list_2

lis = [3, 4,5,7,34,4,1,6,7,2,8,30,20,4,4,4,4,4,4,4,4,4]

peak(lis)