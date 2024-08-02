# print(123)
# print(456)
# print(789)

first = input("Введите число: ")
second = input("Введите число: ")
third = input("Введите число: ")
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
     print(2)
else:
    print(0)






