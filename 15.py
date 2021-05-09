lst = [x for x in range(100)]

print(lst)

gnr = (x for x in range(100))
i = gnr.next()
print(i)

