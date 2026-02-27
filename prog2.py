tup=(23,12,11,8,25)
print("Initial Tuple : ",tup)
'''
lst=list(tup)
lst.sort()
res=tuple(lst)
print("Sorted Tuple : ",res)
'''
res=tuple(sorted(tup))
print("Sorted Tuple :",res)
