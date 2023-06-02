import os#載入一個作業系統


#讀取檔案
def read_file(filename):#確定有找到檔案在去read file
	products = []
	with open(filename, "r", encoding = "big5") as f:#讀取檔案
		for line in f:#把products.csv 裡面的逐筆丟進line變數裡面
			if "商品,價格" in line:
				continue#商品跟價格 在 line 裡面那就跳過這一行
			name,price = line.strip().split(",")#用split() 把 逗點分割,用strip()把換行符號刪除
			products.append([name,price])
	return products


#讓使用者輸入
def user_input(products):
	while True:
		name = input("請輸入商品名稱:")
		if name == "q":
			break
		price = input("請輸入商品價格:")
		products.append([name,price])#可以簡寫為products.append([name,price])
	return products
#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], "的價格是", p[1])#print(p)

#寫入檔案
def write_file(filename,products):
	with open(filename, "w", encoding = "big5") as f:#把資料寫入products.csv
		f.write("商品,價格\n")
		for p in products:#因為不知道products 是什麼所以要投一個products 近來
			f.write(p[0] + "," + p[1] + "\n")#把p[0] 跟p[1] 用逗號拆開就會變成不同格，如果沒有用逗號拆開 會在同一格



def main(filename):
	if os.path.isfile(filename):#檢查檔案在不再
		print("yeah!找到檔案了!")
		products = read_file(filename)#return 回傳到products
	else:
		print("找不到檔案......")

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main("products.csv")