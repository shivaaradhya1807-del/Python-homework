file=open("shoppinglist.txt","w")
file.write("1.get pizza ingredients \n")
file.write("2.buy milk \n")
file.write("3.buy food\n")
file.close()
print("shoppinglist list saved to shoppinglist.txt")

file=open("shoppinglist.txt","r")
content=file.read()
print("===== SHOPPING LIST =====")
print(content)
file.close()

file= open("shoppinglist.txt","r")
lines=file.readlines()
print(f"you have {len(lines)} items in your shopping list.")
file.close()

file=open("shoppinglist.txt","a")
file.write("4. buy a new dress \n")
file.write("5. buy new phone")
file.close()

file= open("shoppinglist.txt","r")
print("====new shopping list ===")
print(file.read())
file.close




