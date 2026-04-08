orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

even_orders = []

for order_id, name in orders:
    if order_id % 2 == 0:
        even_orders.append((order_id, name))

print(even_orders)