LIST = [1, 2, 3, 4, 5]
filters = []
filters.append(lambda x: x > 3 )
filters.append(lambda x: x % 2 == 0)
for f in filters:
    LIST = filter(f, LIST)
print(list(LIST))
