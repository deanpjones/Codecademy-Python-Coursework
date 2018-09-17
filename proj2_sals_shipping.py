#SAL'S SHIPPING
#PROJECT #2
#CODE ACADEMY 
#PROGRAMMING WITH PYTHON 
#Dean Jones, Jul.25, 2018

#----------------
# Ground Shipping
# Weight of Package	                                Price per Pound	    Flat Charge
# 2 pounds or less  	                            $1.50               $20.00
# Over 2 pounds but less than or equal to 6 pounds	$3.00	            $20.00
# Over 6 pounds but less than or equal to 10 pounds	$4.00	            $20.00
# Over 10 pounds	                                $4.75	            $20.00

# Drone Shipping
# Weight of Package	                                Price per Pound	    Flat Charge
# 2 pounds or less	                                $4.50	            $00.00
# Over 2 pounds but less than or equal to 6 pounds	$9.00	            $00.00
# Over 6 pounds but less than or equal to 10 pounds	$12.00	            $00.00
# Over 10 pounds	                                $14.25	            $00.00

# Premium Ground Shipping
# Flat charge: $125.00
#----------------

#FUNCTION: CURRENCY FORMAT
def currency(num):
  return '${:,.2f}'.format(num)

#FUNCTION: CALC COST (helper function)
def calc_cost(price_per_pound, weight, flat_fee):
  return (price_per_pound * weight) + flat_fee

#FUNCTION: COST (GROUND SHIPPING)
#They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. 
def cost_ground_shipping(weight):
  if (weight <= 2.0):
    return calc_cost(1.50, weight, 20.00)
  elif (weight <= 6.0):
    return calc_cost(3.00, weight, 20.00)
  elif (weight <= 10.0):
    return calc_cost(4.00, weight, 20.00)
  elif (weight > 10.0):
    return calc_cost(4.75, weight, 20.00)
  else:
    return "Error: cost_ground_shipping() function"
#TEST: cost_ground_shipping(8.4)
#53.6  
print("Ground Shipping: 8.4lbs should be $53.60")
print(cost_ground_shipping(8.4))
#formatted with function
print(currency(cost_ground_shipping(8.4)))
  
  
#VARIABLE: COST (PREMIUM SHIPPING)
#Premium ground shipping, which is a much higher flat charge, but you aren't charged for weight.
flat_fee_premium_shipping = 125.00

#FUNCTION: COST (DRONE SHIPPING)
#They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
def cost_drone_shipping(weight):
  if (weight <= 2.0):
    return calc_cost(1.50 * 3, weight, 0.00)
  elif (weight <= 6.0):
    return calc_cost(3.00 * 3, weight, 0.00)
  elif (weight <= 10.0):
    return calc_cost(4.00 * 3, weight, 0.00)
  elif (weight > 10.0):
    return calc_cost(4.75 * 3, weight, 0.00)
  else:
    return "Error: cost_drone_shipping() function"
#TEST: cost_drone_shipping(1.5)
#6.75  
print("Drone Shipping: 1.5lbs should be $6.75")
print(cost_drone_shipping(1.5))
#formatted with function
print(currency(cost_drone_shipping(1.5)))

#ENUM (for shipping)
#from enum import Enum
#class ShippingType(Enum):
#	GROUND = 1
#  PREMIUM = 2
#  DRONE = 3
  
#FUNCTION: FIND CHEAPEST (SHIPPING METHOD)
def find_cheapest_shipping(weight):
  result = ""
  a = cost_ground_shipping(weight)
  a_currency = currency(a)
  a_message = "Grounding is the cheapest, costing: {}".format(a_currency)
  b = flat_fee_premium_shipping
  b_currency = currency(b)
  b_message = "Premium is the cheapest, costing: {}".format(b_currency)
  c = cost_drone_shipping(weight)
  c_currency = currency(c)
  c_message = "Drone is the cheapest, costing: {}".format(c_currency)
  
  #compare (a and b)
  if(a < b):		#means (can't be b)
    #compare (a and c)
    if(a < c):
      #print a
      result = a_message
    else:
      #print c
      result = c_message
  elif(a > b):	#means (can't be a)
    #compare (b and c)
    if(b < c):
      #print b
      result = b_message
    else:
      #print c
      result = c_message
  return result
#TEST: find_cheapest_shipping(1.5)
print("Cheapest Shipping for: 1.5lbs")
print(find_cheapest_shipping(1.5))
#TEST: find_cheapest_shipping(4.8)
print("Cheapest Shipping for: 4.8lbs")
print(find_cheapest_shipping(4.8))
#TEST: find_cheapest_shipping(41.5)
print("Cheapest Shipping for: 41.5lbs")
print(find_cheapest_shipping(41.5))