my_tuple = tuple()
my_tuple2 = ()

my_tuple = (35, 1.77, "John", "Doe")
my_tuple2 = (18, 1.75, "Bill", "Gates")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-5]) IndexError

print(my_tuple.count(35))
print(my_tuple.index("John"))

# my_tuple[1] = 1.80
# print(my_tuple) # TypeError: 'tuple' object does not support item assignment

print(my_tuple + my_tuple2)

my_sum_tuple = my_tuple + my_tuple2
print(my_sum_tuple)

print(my_sum_tuple[2:5])

my_sum_tuple = list(my_sum_tuple)
print(type(my_sum_tuple))

my_sum_tuple[1] = 1.81
my_sum_tuple.insert(4, "Smith")
print(my_sum_tuple)

del my_sum_tuple
# print(my_sum_tuple) # NameError: name 'my_sum_tuple' is not defined