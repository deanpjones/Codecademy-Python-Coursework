#CARLY'S CLIPPERS (WEEK 5, DAY 3)
#PROJECT #6
#CODE ACADEMY
#PROGRAMMING WITH PYTHON
#Dean Jones, Aug.06, 2018

# In this project, you will be working for a hair salon called Carly's Clippers. 
# You will be using what you have learned about loops to help process some of Carly's data. 
# To complete the project, you will need to understand how to iterate through lists using for, 
# and how to use list comprehensions to create lists. As an added bonus, you'll refresh your knowledge 
# of basic Python syntax and list operations. If you get stuck or confused, remember that your Slack community 
# is there to help!

# ---------
# You are the data analyst at Carly's Clippers, the newest hair salon on the block. 
# Your job is to go through the lists of data that have been collected in the past couple of weeks. 
# You will be calculating some important metrics that Carly can use to plan out the operation of the business 
# for the rest of the month.

# You have been provided with three lists:

# hairstyles:   the names of the cuts offered at Carly's Clippers
# prices:       the price of each hairstyle in the hairstyles list
# last_week:    the number of each hairstyle in hairstyles that was purchased last week


#FUNCTION: CURRENCY FORMAT 
def currency(num):
  return '${:,.2f}'.format(num)

#HAIRSTYLES: the names of the cuts offered at Carly's Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#PRICES: the price of each hairstyle in the hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#LAST_WEEK: the number of each hairstyle in hairstyles that was purchased last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

#NOTE, there is an ERROR (last_week length is too long)
#print("# of styles: ", len(hairstyles))		#8
#print("# of prices: ", len(prices))				#8
#print("# of last week: ", len(last_week))	#9

#TOTAL_PRICE: sum of all the prices of haircuts 
total_price = 0
total_price = sum(x for x in prices)

#AVERAGE_PRICE: total price divided by number of cuts
average_price = 0
average_price = total_price / len(prices)
print("Average price: ", currency(average_price))

#NEW_PRICES: discounted (each by $5)
new_prices = [x - 5 for x in prices]
print("New prices: ", new_prices)

#TOTAL_REVENUE: how much revenue last week?
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total revenue: ", currency(total_revenue))

#AVERAGE DAILY REVENUE: total_revenue / 7 (days a week)
average_daily_revenue = total_revenue / 7
print("Avg daily revenue: ", currency(average_daily_revenue))

#ADVERTISEMENT (CUTS UNDER $30)
#cuts_under_30 = [hairstyles[i] for i in range(0, #len(hairstyles)) if new_prices[i] < 30]
#print("Hairstyles for under $30: ", cuts_under_30)
cuts_under_30 = [[x, y] for x, y in zip(hairstyles, new_prices) if y < 30]
print("Hairstyles for under $30: ", cuts_under_30)
