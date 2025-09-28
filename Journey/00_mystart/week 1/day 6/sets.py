my_set = set()
my_set2 = {} # This is a dictionary, not a set

print(type(my_set))

my_set2 = {35, 1.77, "John", "Doe"}
print(type(my_set2))

print(len(my_set2))
# print(my_set2[0]) # TypeError: 'set' object is not subscriptable

my_set2.add("New Element")
print(my_set2) # Order is not guaranteed

my_set2.add("John") # No error, but no duplicate added
print(my_set2)

print("Doe" in my_set2)
print("Smith" in my_set2)

my_set2.remove("Doe")
print(my_set2)

my_set2.clear()
print(my_set2)

del my_set2
# print(my_set2) # NameError: name 'my_set2' is not defined

my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "Java", "C++"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_set).union({"New Element"}))

print(my_new_set.difference(my_set)) # Elements in my_new_set but not in my_set