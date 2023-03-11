row1 = ["🧇", "🧇","🧇"]
row2 = ["🧇", "🧇","🧇"]
row3 = ["🧇", "🧇","🧇"]

row = [row1 , row2 , row3]
print (f"{row1}\n {row2} \n {row3}")

posi = input("Where do you want to put the treasure? ")
col = int(posi[0])
rowm = int(posi[1])

row[rowm - 1][col - 1] = "X"

print (f"{row1}\n {row2} \n {row3}")
