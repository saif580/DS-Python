my_list=['Andy','Douglas','Allen','Richard','Andy']

for i in my_list:
    print(i)
list2=[]
count=0
while count<4:
    list2.append(input("Enter the value "));
    count+=1;
print(list2)

print(list2[1:3])   
list2.extend(my_list)
print(list2)
print(my_list.index('Douglas'))
my_list.remove("Richard")
print(my_list)
print(my_list.count("Andy"))
print(len(list2),len(my_list))
print(max(my_list),min(my_list))