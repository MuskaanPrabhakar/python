val = [1,2,3,4]
#for key,num in enumerate(val,0):
    #val[key]= num*2
#print(val) #list is mutable so the original list is modified
#new_val= [x for x in val if x%2!=0] #comprehension list
for num in val:
    if num%2==0:
        val.remove(num)
print(val)

