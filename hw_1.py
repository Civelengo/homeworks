first_list = [1,3,5,7,9]
second_list = [0,2,4,6,8]

mylist= first_list + second_list
mylistx2 = []
for i in mylist:   
    mylistx2.append(i * 2)

for i in mylistx2:
    print(type(i))
