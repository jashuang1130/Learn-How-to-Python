# Desert Menue
# from math import sum
print ''
print '+--------[ Desert Menu ]---------+'
print '| 1. Tiramisu            $ 10.00 |'
print '| 2. Pompei              $ 10.50 |'
print '| 3. Tortina Di Frutta   $ 11.00 |'
print '| 4. Pera Con Gelato      $ 8.50 |'
print '| 5. Gelato & Sorbetto    $ 9.00 |'
print '| 6. Creme Brulee         $ 9.00 |'
print '| 7. Biscotti             $ 8.00 |'
print '| 8. Cannoli Arancio      $ 7.00 |'
print '|                                |'
print '+---------- ENJOY!! -------------+'
print ''

desert_name = {'1': 'Tiramisu', '2': 'Pompei', '3':'Tortina Di Frutta', '4': 'Pera Con Gelato',
'6': 'Creme Brulee', '7':'Biscotti', '8':'Cannoli Arancio'}
desert_price = {'1': 10.00 , '2': 10.50 , '3': 11.00, '4': 8.50, '5': 9.00, '6': 9.00,
'7': 8.00, '8': 7.00}

ordered_list = []

desert_num = input("How many deserts would you like to order? : ")

while desert_num > 0:
	choice = raw_input("Please select the number from desert menue : ")
	ordered_list.append(choice)
	desert_num = desert_num - 1

total_cost = 0.00
print "You've ordered items"
for item in ordered_list:
	print desert_name[item]
	total_cost = desert_price[item] + total_cost

# print "The total cost will be " + str(round(total_cost,2)) + " dollars"
# or  .2f the number to two decimals
print "The total cost will be $%.2f dollars" % total_cost
