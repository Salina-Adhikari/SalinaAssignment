from collections import OrderedDict


grocery_list = OrderedDict()


grocery_list["Fruits"] = ["Apple", "Banana", "Orange"]
grocery_list["Vegetables"] = ["Carrot", "Spinach", "Tomato"]
grocery_list["Dairy"] = ["Milk", "Cheese", "Yogurt"]


print("Grocery List:")
for category, items in grocery_list.items():
    print(f"{category}: {', '.join(items)}")


grocery_list["Snacks"] = ["Chips", "Cookies"]


print("\nUpdated Grocery List:")
for category, items in grocery_list.items():
    print(f"{category}: {', '.join(items)}")
