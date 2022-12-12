# Преобразовать набора списков в другой набор
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
l1, l2, l3 = map(list, zip(users, ids, salary))
print(l1)
print(l2)
print(l3)
users, ids, salary = map(list, zip(l1, l2, l3))
print(users)
print(ids)
print(salary)
