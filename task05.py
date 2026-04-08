numbers = (3, 6, 7, 8, 10, 11)
juft = ()
for son in numbers:
    if son % 2 == 0:
        juft += (son,)
print(juft)