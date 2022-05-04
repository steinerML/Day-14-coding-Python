# HBO exercise
#Library shipping costs with discounts and different shipping costs depending on total order.

def total_cost (order,selling_price,shipping_1st,shipping_others,discount):
    purchase_price = selling_price * (1 - discount)
    cost = (order * purchase_price) + 4 + (order - 1) * shipping_others
    return print('Total cost is: ', round(cost,2))

order = 50
selling_price = 19.95
shipping_1st = 4
shipping_others = 0.80
discount = 0.42

result = total_cost (order,selling_price,shipping_1st,shipping_others,discount)