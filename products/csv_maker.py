import pandas as pd

product_name = []
price = []
ordered_quantity = []
total_amount = []

for i in range(int(input("ENTER NO OF ORDERS: "))):
    product_name.append(input("ENTER PRODUCT NAME: "))
    price.append(int(input("ENTER PRICE: ")))
    ordered_quantity.append(int(input("ENTER QUANTITY: ")))
    total_amount.append(int(input("ENTER AMOUNT: ")))

dic = {
    'product_name': product_name,
    'price': price,
    'ordered_quantity': ordered_quantity,
    'total_amount': total_amount,
}

orders_list = pd.DataFrame(dic)
orders_list.to_csv('order_list.csv')
