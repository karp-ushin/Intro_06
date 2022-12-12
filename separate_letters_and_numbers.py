# Дан список, вывести отдельно буквы и цифры.
a = ["a", 'b', '2', '3', 'c']
b = filter(str.isalpha, a)
print(*b)
c = filter(str.isdigit, a)
print(*c)
