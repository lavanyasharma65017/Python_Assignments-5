lst=[]
for i in range(1,11):
    lst.append(i)
print("Original list:",lst)

first_five=lst[:5]
print("Extracted first five elements:",first_five)

reverse_lst=first_five[::-1]
print("Reversed extracted elements:",reverse_lst)