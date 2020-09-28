# # previous homework
# # task2 #method1
# lst=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
# new_lst=[]
# new_set=set()
# for i in lst:
# 	t=tuple(i)
# 	if t not in new_set:
# 		new_lst.append(i)
# 		new_set.add(t)
# print(new_lst)
# # #method2
# # lst=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
# # new_lst=[]
# # for i in lst:
# # 	if i not in new_lst:
# # 		new_lst.append(i)
	
# # print(new_lst)		

# #task3
# original_list=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
# new_list=[]
# def flatten(I):
# 	for i in I:
# 		if type(i)==list:
# 			flatten(i)
# 		else:
# 			new_list.append(i)    	
# flatten(original_list)
# print(new_list)
# #task4
# my_list=[1,1,2,3,4,4,5,1]
# b=0
# my_list_2=[]
# for i in range(len(my_list)):
# 	if i % 3==0:
# 		if i==0:
# 			continue
# 		my_list_2.append(list(my_list[b:3]))
# 		b+=3
# for i in range(len(my_list[b:i])):
# 	my_list_2.append(list(my_list[3:8]))
# print(my_list_2)	
			
# #task5
# a=int(input("Enter a number upto 26\n"))
# b="5"
# c=b/a
# print(c)
# try:
# 	if a>26:
# 		raise ValueError(a,"is out of allowed range")
# 	if a==0:
# 	    raise ZeroDivisonError("Division by 0 is not excepted")	
# except ValueError as v:
# 	print(v)	
# except ZeroDivisonError as z:
#     print(z)
# except TypeError:
#     print("Unsupported operation")    		
# else:
#     print(a,"is within the allowed range")	

# #today's homework.
# #task1
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4={6:50,7:60}
# dict5={}
# for i in (dict1,dict2,dict3,dict5):
# 	dict5.update(i)
# print(dict5)
# #task2
# n=5
# d=dict()
# for i in range(n+1):
# 	d[i]=i*i
# print(d)	
# #task3
original_dic={"c1":"red","c2":"green","c3":None}
new_dic={}
for i in original_dic:
	print(i)
	print(len(i))

	if len(i)>0:
		print(new_dic)
		new_dic.update(i)
print(new_dic, "after update")
print(new_dic)

