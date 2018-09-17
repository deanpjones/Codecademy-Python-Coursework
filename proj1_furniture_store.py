#FURNITURE STORE PROJECT 
#PROJECT #1
#CODE ACADEMY 
#PROGRAMMING WITH PYTHON 
#Dean Jones, Jul.18, 2018

#FUNCTION: calculate tax
def calc_tax(total, tax):
    return total * tax

#FUNCTION: calculate grand total
def calc_gtotal(total, tax):
    my_tax = calc_tax(total, tax)
    return total + my_tax

#FUNCTION: print receipt
def print_receipt(name, items, total, tax_percent, tax_owed, gtotal):
    print("\n***********************")
    print(name)                                         #print customer name
    
    print("Items: ")
    print(items)                                        #print items list

    print("Total: $" + str(total))                      #total

    tax_formatted = format(tax_percent * 100, '.2f')    #tax
    print("Tax: " + str(tax_formatted) + "%")

    tax_owed_formatted = format(tax_owed, '.2f')        #tax owed
    print("Tax Owed: $" + str(tax_owed_formatted))                

    gtotal_formatted = format(gtotal, '.2f')            #grand total
    print("Grand Total: $" + str(gtotal_formatted))

    print("***********************\n")
    return


#variables
#loveseat
lovely_loveseat_price = 254.00
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
#settee
stylish_settee_price = 180.50
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
#lamp
luxurious_lamp_price = 52.15
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
#tax
sales_tax = 0.088

#-------------------
#first customer
customer_one_total = 0 					#running total
customer_one_itemization = ""		#descriptions
customer_one_tax = 0
customer_one_gtotal = 0
#purchase 1
customer_one_total += lovely_loveseat_price 	
customer_one_itemization += lovely_loveseat_description
#purchase 2
customer_one_total += luxurious_lamp_price 
customer_one_itemization += luxurious_lamp_description

#checkout 
#add tax
customer_one_tax = calc_tax(customer_one_total, sales_tax)
#customer_one_tax = customer_one_total * sales_tax

#grand total (with tax)
customer_one_gtotal = calc_gtotal(customer_one_total, sales_tax)
#customer_one_gtotal = customer_one_total + customer_one_tax

#print receipt
print_receipt("Customer One", customer_one_itemization, customer_one_total, sales_tax, customer_one_tax, customer_one_gtotal)
# print("\n***********************")
# print("Customer One")
# print("Items: ")
# print(customer_one_itemization)
# print("Total: $" + str(customer_one_total))
# tax_formatted = format(sales_tax * 100, '.2f')
# print("Tax: " + str(tax_formatted) + "%")
# gtotal_formatted = format(customer_one_gtotal, '.2f')
# print("Grand Total: $" + str(gtotal_formatted))
# print("***********************\n")
#-------------------
#-------------------
#second customer
customer_two_total = 0 					#running total
customer_two_itemization = ""		#descriptions
customer_two_tax = 0
customer_two_gtotal = 0
#purchase 1
customer_two_total += stylish_settee_price 	
customer_two_itemization += stylish_settee_description
#purchase 2
customer_two_total += luxurious_lamp_price 
customer_two_itemization += luxurious_lamp_description

#checkout 
#add tax
customer_two_tax = calc_tax(customer_two_total, sales_tax)
#customer_two_tax = customer_two_total * sales_tax

#grand total (with tax)
customer_two_gtotal = calc_gtotal(customer_two_total, sales_tax)
#customer_two_gtotal = customer_two_total + customer_two_tax

#print receipt
print_receipt("Customer Two", customer_two_itemization, customer_two_total, sales_tax, customer_two_tax, customer_two_gtotal)
# print("\n***********************")
# print("Customer Two")
# print("Items: ")
# print(customer_two_itemization)
# print("Total: $" + str(customer_two_total))
# tax_formatted2 = format(sales_tax * 100, '.2f')
# print("Tax: " + str(tax_formatted2) + "%")
# gtotal_formatted2 = format(customer_two_gtotal, '.2f')
# print("Grand Total: $" + str(gtotal_formatted2))
# print("***********************\n")
#-------------------

