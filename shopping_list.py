items = {}
income = float(input('Enter your income : '))
totalItemPrice = 0
print('PRESS ENTER TO ADD ITEMS')
print('###############################')
itemName = input('Item name : ')
itemPrice = float(input('Item price : '))
items.update({itemName: itemPrice})
totalItemPrice += itemPrice
print()
print('Remaining balance : {0}'.format(income - totalItemPrice))
choice = "y"

while totalItemPrice <= income and choice == "y".lower():
    print()
    choice = input('Do you want to enter more item? (y/N) : ')
    if choice == 'y':
        itemName = input('Item name : ')
        itemPrice = float(input('Item price : '))
        items.update({itemName: itemPrice})
        totalItemPrice += itemPrice
        print()
        if (income - totalItemPrice)>=0:
            print('Remaining balance : {0}'.format(income - totalItemPrice))

if totalItemPrice > income:
    print('Insufficient balance')
    print()
    print('ITEMS IN YOUR LIST')
    print('-------------------')
    print(items)
else:
    print('Thanks for using....')
    print()
    print('ITEMS IN YOUR LIST')
    print('-----------------------------------------------')
    print('ITEM NAME'.ljust(15),'|'.ljust(10),'ITEM PRICE')
    print('-----------------------------------------------')
    for key in items:
        print(key.ljust(15),'|'.ljust(10),items[key])
        print('-----------------------------------------------')
    print("TOTAL".ljust(15),'|'.ljust(10),totalItemPrice)
input()
