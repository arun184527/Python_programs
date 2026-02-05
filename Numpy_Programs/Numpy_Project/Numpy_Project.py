import numpy as np
STORE_NAME = "Big Bazaar"
GST_RATE = 0.18

items = np.array([
    ["Rice",     40,  55, 1000, 0, "INDIA GATE",     "15-08-2026"],
    ["Sugar",    38,  50,  800, 0, "EID PARRY",      "10-10-2025"],
    ["Oil",     120, 150,  500, 0, "Sunflower",      "24-12-2025"],
    ["Milk",     25,  30,  300, 0, "Nandini Milk",   "27-09-2024"],
    ["Curd",     45,  60,  600, 0, "Masti Curd",     "15-11-2024"],
    ["Salt",     20,  25,  400, 0, "TATA",           "15-08-2026"],
    ["Shampoo", 150, 200,  200, 0, "Himalaya",       "09-05-2025"],
    ["Soap",     30,  40,  500, 0, "Yardley London", "29-07-2025"],
    ["Coldrink", 60,  80,  300, 0, "Coca Cola",      "31-12-2024"]
], dtype=object)


def view_items():
    print("\n----- ITEM DETAILS -----")
    incoming = items[:, 3].astype(int)
    sold = items[:, 4].astype(int)
    remaining = incoming - sold
    for i in range(len(items)):
        print(f"\nItem Name     : {items[i][0]}")
        print(f"Cost Price   : Rs {items[i][1]}")
        print(f"Sell Price   : Rs {items[i][2]}")
        print(f"Incoming Qty : {incoming[i]}")
        print(f"Sold Qty     : {sold[i]}")
        print(f"Supplier     : {items[i][5]}")
        print(f"Expiry Date  : {items[i][6]}")
        print(f"Remaining    : {remaining[i]}")
        print("-------------------------")


def sell_item():
    name = input("Enter Item Name: ").strip().lower()
    brand = input("Enter Brand Name: ").strip().lower()
    qty = int(input("Enter Quantity: "))
    for i in range(len(items)):
        if (items[i][0].lower() == name and
            items[i][5].lower() == brand):
            incoming = int(items[i][3])
            sold = int(items[i][4])
            remaining = incoming - sold
            if qty <= remaining:
                items[i][4] = sold + qty
                base = int(items[i][2]) * qty
                gst = base * GST_RATE
                total = base + gst
                print("\n----- CUSTOMER BILL -----")
                print("Store       :", STORE_NAME)
                print("Item        :", items[i][0])
                print("Brand       :", items[i][5])
                print("Quantity    :", qty)
                print("Base Amount :", base)
                print("GST (18%)   :", gst)
                print("Total       :", total)
                print("--------------------------")
            else:
                print(" Not enough stock!")
            return
    print(" Item not found!")


def total_profit():
    cost = items[:, 1].astype(int)
    sell = items[:, 2].astype(int)
    sold = items[:, 4].astype(int)
    profit = np.sum((sell - cost) * sold)
    print("\n TOTAL PROFIT: Rs", profit)


def total_gst():
    sell = items[:, 2].astype(int)
    sold = items[:, 4].astype(int)
    gst = np.sum(sell * sold * GST_RATE)
    print("\n TOTAL GST COLLECTED: Rs", gst)



def sealed_stock():
    cost = items[:, 1].astype(int)
    incoming = items[:, 3].astype(int)
    sold = items[:, 4].astype(int)
    remaining = incoming - sold
    value = remaining * cost
    print("\n----- SEALED STOCK VALUE -----")
    for i in range(len(items)):
        print(f"\nItem      : {items[i][0]}")
        print(f"Remaining : {remaining[i]}")
        print(f"Value     : Rs {value[i]}")
        print("-----------------------------")



def highest_profit():
    cost = items[:, 1].astype(int)
    sell = items[:, 2].astype(int)
    sold = items[:, 4].astype(int)
    profit = (sell - cost) * sold
    if np.max(profit) == 0:
        print("\nNo sales yet!")
        return
    index = np.argmax(profit)
    print("\n Highest Profit Item:", items[index][0])
    print("Profit: Rs", profit[index])


def add_item():
    global items
    name = input("Item Name: ")
    cost = int(input("Cost Price: "))
    sell = int(input("Selling Price: "))
    qty = int(input("Quantity: "))
    supplier = input("Supplier: ")
    expiry = input("Expiry Date: ")
    new_item = np.array(
        [name, cost, sell, qty, 0, supplier, expiry],
        dtype=object
    )
    items = np.vstack((items, new_item))
    print("\n Item Added Successfully! ")



while True:
    print("\n===== BIG BAZAAR SYSTEM =====")
    print("1. View Items")
    print("2. Sell Item")
    print("3. Total Profit")
    print("4. Total GST")
    print("5. Sealed Stock Value")
    print("6. Highest Profit Item")
    print("7. Add New Item")
    print("8. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        view_items()
    elif choice == 2:
        sell_item()
    elif choice == 3:
        total_profit()
    elif choice == 4:
        total_gst()
    elif choice == 5:
        sealed_stock()
    elif choice == 6:
        highest_profit()
    elif choice == 7:
        add_item()
    elif choice == 8:
        print("\n Thank You for Using Big Bazaar System ")
        break
    else:
        print("Invalid Choice!")