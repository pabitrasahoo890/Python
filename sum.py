# list = [11,22,33,44,55,66]
# list2 = eval(input("enter a list: "))
# count = 0
# for i in range(0,len(list)):
#     count = count + list[i]
# print(count)

# list1 = [52,82,46,9,28,53,33]
# list1 = eval(input("enter a list: "))
# min = list1[0]
# for i in range(0,len(list1)):
#     if(list1[i] < min ):
#         min = list1[i]
# print(min)

# list2 = [52,82,46,9,28,53,33]
# list2 = eval(input("enter a list: "))
# max = list2[0]
# for i in range(0,len(list2)):
#     if(list2[i] > max ):
#         max = list2[i]
# print(max)


# list3 = eval(input("enter a list: "))
# count = 0
# for i in range(0,len(list3)):
#     count = count+1
# print(count)

# list4 = eval(input("enter a list: "))
# for i in range(0,len(list4)):
#     for j in range(i+1,len(list4)):
#         if(list4[i] > list4[j]):
#             list4[i],list4[j] = list4[j],list4[i]
# print(list4)


a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
