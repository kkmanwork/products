products = []
while True:
	name = input("請輸入商品名稱:")
	if name == "q":
		break
	price = input("請輸入商品價格:")
	p = []
	p.append(name)
	p.append(price)
	# p = [name, price]可以簡略寫
	products.append(p)#可以簡寫為products.append([name,price])
print(products[0][1])#讀取0大清單中的1小清單位置
for p in products:
	print(p[0], "的價格是", p[1])
	#print(p)