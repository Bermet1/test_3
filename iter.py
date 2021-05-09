# Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз

lst = [5, 10, 6, 3, -2]
for i in lst:
    print(i)

# iter
iter1 = iter(lst)
print(next(iter1))

# enumerate
enum = enumerate(lst)
print(next(enum))
