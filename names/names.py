import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
# print('names_1', names_1)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = [i for i in names_1 + names_2 if i not in names_1 or i not in names_2]
s = ", "
y = s.join(duplicates)
r = str(y)
print('y', y)
duplicates.append(y)








# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# my code

# def Diff(li1, li2):
    # .join()

# x = [i for i in names_1 + names_2 if i not in names_1 or i not in names_2]
# print('x',x)
# s = ", "
# y = s.join(x)
# r = str(y)
# print('y', y)
# duplicates.append(y)





    # return duplicates

# Diff(names_1, names_2)









end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
