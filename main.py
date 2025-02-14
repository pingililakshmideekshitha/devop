old_dict={'A':67,'B':23,'C':45,'D':56,'E':12,'F':69,'G':68,'H':24}
new_dict=dict((value,key)for key, value in  old_dict( ))
print("original dictionary is:")
print(old_dict)
print()
print("dictionary after swapping is:")
print("keys:values")
for i in new_dict:
    print(i," ",new_dict[i])
