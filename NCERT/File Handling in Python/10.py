import pickle

n = int(input("Enter numberof records: "))

with open("records.dat", "wb+") as file:
    for i in range(1, n+1):
        print(f"For Item No {i}:")
        Item_Name = input("Enter Item Name: ")
        Qty = float(input("Enter Quantity: "))
        Price = float(input("Enter Price: "))
        print()
        
        pickle.dump([i, Item_Name, Qty, Price], file)

template = ("Item No: ", "Item Name: ", "Quantity: ", "Price per Item: ", "Amount: ")

try:
    with open("records.dat", "rb") as file:
        while True:
           dat = pickle.load(file)

           for i in range(5):
               print(template[i], end="")
               if i != 4: print(dat[i])
               else: print(dat[2]*dat[3])
           print()

except EOFError: pass