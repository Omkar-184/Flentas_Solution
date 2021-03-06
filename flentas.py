# -*- coding: utf-8 -*-
"""Flentas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JevRgJtj_84eV8WkpDbYGk2XKGgkm_BU
"""

# minimum cost function 
def minCost(price, n): 

	# Sort the price array 
	price = sorted(price) 
	totalCost = 0

	for i in range(n - 1, 1, -2): 
		if (i == 2): 
			totalCost += price[2] + price[0] 

		else: 	 
			p1 = price[i] + price[0] + 2 * price[1] 
			p2 = price[i] + price[i - 1] + 2 * price[0] 
			totalCost += min(p1, p2) 

	#minimum price  
	if (n == 1): 
		totalCost += price[0] 

	else: 
		totalCost += price[1]

	return totalCost 


price = []
n = int(input('enter number of persons:: '))
print('Enter the cost of person::')
for i in range(int(n)):
  k = int(input(''))
  price.append(k)
print("The prices are:: ", price)

print(minCost(price, n))