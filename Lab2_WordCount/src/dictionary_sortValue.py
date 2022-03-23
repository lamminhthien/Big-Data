orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])

test = "ABCDAS	1"
word,count = test.split('\t',1)
print(word)
print(int(count))

current_word = None
if current_word:
	print('yes')
else:
	print('no')