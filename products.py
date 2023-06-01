#讀取檔案
products = []
with open("products.csv", "r", encoding = "big5") as f:
	for line in f:#把products.csv 裡面的逐筆丟進line變數裡面
		if "商品,價格" in line:
			continue#商品跟價格 在 line 裡面那就跳過這一行
		name,price = line.strip().split(",")#用split() 把 逗點分割,用strip()把換行符號刪除
		products.append([name,price])
print(products)

#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])
	#print(p)

#寫入檔案
with open("products.csv", "w", encoding = "big5") as f:#把資料寫入products.csv
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")#把p[0] 跟p[1] 用逗號拆開就會變成不同格，如果沒有用逗號拆開 會在同一格