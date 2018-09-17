#REGGIE'S LINEAR REGRESSION
#PROJECT #7
#CODE ACADEMY
#PROGRAMMING WITH PYTHON
#Dean Jones, Aug.09, 2018

# Project: Linear Regression
# Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit 
# in the play area. As such, he is working on researching the bounciness of different balls so as to optimize 
# the pit. He is running an experiment to bounce different sizes of bouncy balls, and then fitting lines to the 
# data points he records. He has heard of linear regression, but needs your help to implement a version 
# of linear regression in Python.

# Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles 
# that group of points. A good Linear Regression algorithm minimizes the error, or the distance from each point to 
# the line. A line with the least error is the line that fits the data the best. We call this a line of best fit.

# We will use loops, lists, and arithmetic to create a function that will find a line of best fit when given 
# a set of data.

#--------------------
# LINEAR REGRESSION 

#FUNCTION: GET (Y-VALUE)(for a line)
# y = m * x + b     (this formula is a slope of a line)
def get_y(m, b, x):
    return m * x + b

#TEST
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)
#RUN (in powershell)
# PS C:\Users\Pythagoras\Documents\000-Code\code academy\python\07-Project (Reggies Linear Regression)> 
# python .\proj7_reggies_linear_regression.py
# True
# True

#FUNCTION: CALCULATE ERROR
# gets the difference between (a point) and (line)
# eg.   point (3, 4), line (y = x), should be (1 unit away)         #calcutlate_error(1, 0, (3, 4))
#       point (3, 3), line (y = x - 1), should be (1 unit away)     #calcutlate_error(1, -1, (3, 3))
#       point (3, 3), line (y = -x + 1), should be (5 units away)   #calcutlate_error(-1, 1, (3, 3))
# I was confused, but I think it's asking me to get the (difference of the vertical Y-VALUES)
#   from the LINE and the POINT
def calculate_error(m, b, pt):
    x_point = pt[0]
    y_point = pt[1]
    y_value = get_y(m, b, x_point)
    diff = abs(y_point - y_value)       #absolute value
    return diff

#TEST
print(calculate_error(1, 0, (3, 3)))    #returns 0
print(calculate_error(1, 0, (3, 4)))    #returns 1
print(calculate_error(1, -1, (3, 3)))   #1 
print(calculate_error(-1, 1, (3, 3)))   #5

#datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
#FUNCTION: CALCULATE ERROR (from list of points)
def calculate_all_error(m, b, lst):
    result = [calculate_error(m, b, pt) for pt in lst]      #[1, 5, 9, 3]
    return sum(result)
    
#TEST
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
#[0, 0, 0, 0]
print(calculate_all_error(1, 1, datapoints))
#[-1, -1, -1, -1]
print(calculate_all_error(1, -1, datapoints))
#[1, 1, 1, 1]
print(calculate_all_error(-1, 1, datapoints))
#[1, 5, 9, -3]


# ------------------------------------------------------------------------------------------------------------------
# We are going to find the smallest error. First, we will make every possible `y = m*x + b` line by pairing all of the possible `m`s with all of the possible `b`s. Then, we will see which `y = m*x + b` line produces the smallest total error with the set of data stored in `datapoint`.

# First, create the variables that we will be optimizing:
# * `smallest_error` &mdash; this should start at infinity (`float("inf")`) so that any error we get at first will be smaller than our value of `smallest_error`
# * `best_m` &mdash; we can start this at `0`
# * `best_b` &mdash; we can start this at `0`

# We want to:
# * Iterate through each element `m` in `possible_ms`
# * For every `m` value, take every `b` value in `possible_bs`
# * If the value returned from `calculate_all_error` on this `m` value, this `b` value, and `datapoints` is less than our current `smallest_error`,
# * Set `best_m` and `best_b` to be these values, and set `smallest_error` to this error.

# By the end of these nested loops, the `smallest_error` should hold the smallest error we have found, and `best_m` and `best_b` should be the values that produced that smallest error value.

# Print out `best_m`, `best_b` and `smallest_error` after the loops.

# ------------------------------------------------------------------------------------------------------------------
#USE (TRIAL AND ERROR) TO FIND LINE (OF BEST FIT)
#LIST (m - value to try)
possible_ms = [x / 10 for x in range(-100, 100)]
#LIST (b - values to try)possible_asv
possible_bs = [x / 10 for x in range(-200, 200)]

#FUNCTION: TRIAL AND ERROR (FOR SMALLEST ERROR)
def find_smallest_error(lst):
    #variables (defaults)
    smallest_error = float("inf")
    best_m = 0
    best_b = 0

    #loop thru all possible combinations
    for m in possible_ms:
        for b in possible_bs:
            test = calculate_all_error(m, b, lst)
            if (test < smallest_error):
                smallest_error = test   #save best (error value)
                best_m = m              #save best (m - value)
                best_b = b              #save best (b - value)
                #UNCOMMENT (to see all errors - that are less)
                #print("error: {}, m: {}, b: {}".format(smallest_error, best_m, best_b))
    return [smallest_error, best_m, best_b]

#TEST (against 'datapoints' list)
#DIDN'T GET SAME RESULTS?
#NOT [0.30000000000000004 1.7000000000000002 4.999999999999999]
#datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]                    #wrong set... #[0.0, 1.0, 0.0]
# ****************************
#FIX: was using the wrong LIST of DATAPOINTS (thanks @Bobb-uk :) for pointing that out)
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]               #[4.999999999999999, 0.30000000000000004, 1.7000000000000002]
best = find_smallest_error(datapoints)
print("error: {}, m: {}, b: {}".format(best[0], best[1], best[2]))
# ****************************

# -----------
m1 = 0.3
b1 = 1.7
x1 = 6
#test 
get_y(m1, b1, x1)       #3.5