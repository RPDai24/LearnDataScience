# Practical Task 2

# as enum
cappuccino = "Cappuccino"
cortado = "Cortado"
doppio = "Doppio"
latte = "Latte"
mocha = "Mocha"
# cafe menu
menu = [cappuccino, cortado, doppio, latte, mocha]
# cafe stock
stock = {
    cappuccino : 100,
    cortado: 200,
    doppio: 300,
    latte: 400,
    mocha: 500
}
# cafe price
price = {
    cappuccino : 2.0,
    cortado: 3.0,
    doppio: 4.0,
    latte: 5.0,
    mocha: 6.0
}
# caculate the total stock worth in the cafe
item_values = []
for item in menu:
    item_value = stock[item] * price[item]
    item_values.append(item_value)

print(f"The total stock worth: £{sum(item_values)}")