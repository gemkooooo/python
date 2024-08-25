#1st task
from idlelib.replace import replace

immutable_var = 1, "python", True
print(immutable_var)

#2nd task
#immutable_var[0] = 2
#print(immutable_var)

#Ответ: выйдет ошибка, говорящая о том, что в кортеже нельзя менять данные, так как они не изменяемые

#3rd task
mutable_list = [2, "language", False]
mutable_list[1] = "english"
mutable_list.append(3)
mutable_list.extend([1, "soft", True])
print(mutable_list)
