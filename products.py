products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)    # or p = [name, price]
	products.append(p) # or products.append([name, price])
print(products[1][1])
