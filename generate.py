# генератор
def numbers(start, stop, step):
    a = start
    while a < stop:
        yield a
        a += step

for i in numbers(1, 20, 2):
    print(i)


# использование генератора 2 раза

lst = [5, 10, 3, 6]

sqrt_lst = list(i ** 2 for i in lst)

print(sqrt_lst)



