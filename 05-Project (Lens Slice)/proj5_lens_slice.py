#LEN'S SLICE (WEEK 4, DAY 6)
#PROJECT #5
#CODE ACADEMY
#PROGRAMMING WITH PYTHON
#Dean Jones, Aug.02, 2018

# In this project, you will be working for a pizza place called Len's Slice. 
# You will be using your newfound knowledge of lists to keep track of sales data for 
# the store, and help your manager do some research. To complete the project, you will 
# need to understand how to perform basic operations on lists, like len() and slicing. 
# On the way, you'll refresh your knowledge of basic Python syntax. If you get stuck 
# or confused, remember that your Slack community is there to help!

# This project is not graded and you do not need to submit it anywhere. 
# If you would like to check your results, the solution code can be found here.

# ----------------------

# You work at Len's Slice, a new pizza joint in the neighborhood. 
# You are going to use your knowledge of Python lists to organize some of your sales data.

#FUNCTION: HELPER (FUNCTION, PRINT)
def helper(message, func):
  temp = func
  print(message, temp)

#LIST: TOPPINGS 
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#LIST: PRICES 
prices = [2, 6, 1, 3, 2, 7, 2]

#LENGTH (TOPPINGS)
num_pizzas = len(toppings)

#PRINT (# OF TOPPINGS)
print("We sell {} different kinds of pizza!".format(num_pizzas))

#ZIP LISTS 
pizzas = list(zip(prices, toppings))

#SORT (PIZZAS)
pizzas.sort()

#PRINT (PIZZAS)
print("Pizzas: ", pizzas)

#SAVE (CHEAPEST PIZZA)
cheapest_pizza = pizzas[0]
helper("Cheapest pizza: ", cheapest_pizza)

#SAVE (MOST EXPENSIVE PIZZA)
priciest_pizza = pizzas[-1]
helper("MOST EXPENSIVE pizza: ", priciest_pizza)

#SAVE (THREE CHEAPEST PIZZAS)
three_cheapest = pizzas[:3]
helper("3 cheapest pizzas: ", three_cheapest)

#SAVE ($2 DEAL)(SLICES FOR TWO BUCKS - SALE)
#num_two_dollar_slices = pizzas.count('2')		#doesn't work for (2d list)
#COUNT (2D ARRAY)
#num_two_dollar_slices = sum(x.count(2) for x in pizzas)
#just count the (price list)
num_two_dollar_slices = prices.count(2)
helper("num_two_dollar_slices: ", num_two_dollar_slices)