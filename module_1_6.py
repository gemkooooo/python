print("1st global task\n")
my_dict = {'Gennady': 1992, 'Michael': 1993, 'Tatiana': 1969}
#1st task
print(my_dict)
#2nd task
print(my_dict['Gennady'])
#3rd task
my_dict['Vladislav'] = 1969
my_dict['Anna-Maria'] = 2001
print(my_dict)
#4th task
del my_dict['Gennady']
print(my_dict)

print("\n2 global task\n")
my_set = {1, 1, (3, 2), True, False, "Осень", "Лето", "Осень"}
#1st task
print(my_set)
#2nd task
print(my_set.add(4))
print(my_set.add('Зима'))
print(my_set)
#3rd task
print(my_set.remove('Лето'))
print(my_set)
