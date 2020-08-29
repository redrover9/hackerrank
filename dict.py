n = int(input())

phoneBook = {}

for i in range(0, n):
	data = input()
	x = data.split(' ')
	phoneBook[x[0]] = x[1]

l = list(phoneBook)[n - 1]
queries = []
while True:
	try:
		query = input()
		queries.append(query)
	except EOFError:
		break

for j in queries:
	if j in phoneBook:
		print(j + "=" + phoneBook[j])
	else:
		print("Not found")