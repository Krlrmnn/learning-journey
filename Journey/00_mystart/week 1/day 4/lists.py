my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 12]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.73, "Bill", "Gates"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
print(my_other_list.count(35))

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]
print(height)

print(my_other_list + my_list)

my_other_list.append("Enterprise1") # add element to the end of the list
print(my_other_list)

my_other_list.insert(1, "EnterpriseX") # insert at index 1
print(my_other_list)

my_other_list[1] = "Enterprise2" # change element at index 1
print(my_other_list)

my_other_list.remove("Enterprise2") # remove element
print(my_other_list)

my_other_list.pop() # remove last element
print(my_other_list)

#my_other_list.pop(2)
#print(my_other_list)

my_pop_element = my_other_list.pop(2) # remove element at index 2 and return it
print(my_pop_element)
print(my_other_list)

del my_other_list[2] # delete element at index 2
print(my_other_list)

my_new_list = my_list.copy() # copy list
print(my_new_list)

my_new_list.reverse() # reverse list
print(my_new_list)

my_new_list.sort() # sort list
print(my_new_list)

my_list.clear() # clear the list
print(my_list)