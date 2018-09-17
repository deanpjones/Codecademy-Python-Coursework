# BASTA FAZOOLIN ()
# PROJECT #12
# CODE ACADEMY
# PROGRAMMING WITH PYTHON
# Dean Jones, Sep.03, 2018 (finished on Sep.6)(GOOD CHALLENGE!!!)
#
# You've started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin' with My Heart.
# The restaurant has been doing fantastically and seen a lot of growth lately. You've been hired to keep things organized.

# TODO:
# HOW TO TAKE AN ORDER? (like with dropdown on menu)(so I don't have to type it constantly)
# WHAT IF THERE ARE (TWO MENUS)(the times overlap)
#   What if there are TWO items (AT DIFFERENT PRICES)(need something to resolve this conflict)
# CAN I SET THIS UP (TIME BASED) IN A (GRID LIKE NUMBERS)(to resolve these issues?)
# HOW CHECK FOR THE (TIME OF ORDER)


# DATE
# TIME
# MENU
# NAME
# ADDRESS
# PHONE
# RESTAURANT
# ITEM
# ITEMS
# BILL
# FRANCHISE
# BUSINESS


#IMPORTS
import datetime

# CLASS: DATE
class Date:
    #constructor
    def __init__(self, date):
        self.date = date
        self.year = self.date.year
        self.month =  self.date.month
        self.day =  self.date.day
        self.dayOfWeek =  self.date.strftime('%A')
    #string representation
    def __repr__(self):
        return self.date.strftime('%A, %b.%d, %Y')
# d = datetime.date(year=2018, month=9, day=5)
# d.strftime('%A, %b.%d, %Y')         #'Wednesday, Sep.05, 2018'
# d.strftime('%A')                    #'Wednesday'
#SET THE DATE
d = Date(datetime.date(year=1976, month=6, day=7))
# Monday, Jun.07, 1976
#GET THE CURRENT DATE
current = Date(datetime.datetime.now())
# Wednesday, Sep.05, 2018

# CLASS: TIME
# dependencies: (datetime) import
class Time:
    #constructor
    def __init__(self, my_time, descr):
        self.time = my_time.strftime('%I:%M %p')	#'11:00 AM'
        self.description = descr
        self.hour24 = my_time.hour
        self.minute = my_time.minute
        self.day_night = my_time.strftime('%p')
    #string representation
    def __repr__(self):
        return '{}: {}'.format(self.description, self.time)
    # iterable (for x in ...)
    def __iter__(self):
        return iter(self)
#TEST
# t = Time(datetime.time(hour=11, minute=00), 'Start Time')
# t.time                  #'11:00 AM'
# t.description           #'Start Time'
# print(t)                #Start Time: 11:00 AM

# CLASS: MENU
class Menu:
    # constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start = start_time
        self.end = end_time
    # string representation
    def __repr__(self):
        return self.menu_long()
    # items (string repr)
    def items_tostring(self):
        i = ''
        for k,v in self.items.items():
            #i += '\n' + str(k) + ' ' + str(v)
            i += '\n\t{}: {}'.format(k.title(), self.currency(v))
            #print(k, v)
        return i
    # currency format
    def currency(self, num):
        return '${:,.2f}'.format(num)
    # print menu (short)
    def menu_short(self):
        return '{} is available from {} to {}'.format(self.name, self.start.time, self.end.time)
    # print menu (long)
    def menu_long(self):
        #return 'Name: {}\nItems: {}\nStart: {}\nEnd: {}'.format(self.name, self.items, self.start, self.end)
        return 'Name: {}\nItems: {}\nStart: {}\nEnd: {}'.format(self.name, self.items_tostring(), self.start, self.end)
    # iterable (for x in ...)
    def __iter__(self):
        return iter(self.items)

#TEST
# st = Time(datetime.time(hour=11, minute=00), 'Start Time')
# et = Time(datetime.time(hour=16, minute=00), 'End Time')
# m = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00}, st, et)
# m.items                     #{'pancakes': 7.5, 'waffles': 9.0}
# m.name                      #'Brunch'
# m.start_time                #Time OBJECT, Start Time: 11:00 AM
# m.end_time                  #Time OBJECT, End Time: 04:00 PM
# m.end_time.time             #'04:00 PM'
# m.start_time.time           #'11:00 AM'
# m.start_time.description    #'Start Time'
# print(m)
    # Name: Brunch
    # Items: {'pancakes': 7.5, 'waffles': 9.0}
    # Start: Start Time: 11:00 AM
    # End: End Time: 04:00 PM

# create menu (Brunch)
brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
stBrunch = Time(datetime.time(hour=11, minute=00), 'Start Time')
etBrunch = Time(datetime.time(hour=16, minute=00), 'End Time')
mnuBrunch = Menu('Brunch Menu', brunch, stBrunch, etBrunch)

# create menu (Early Bird Dinner)
early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
stEarlyBird = Time(datetime.time(hour=15, minute=00), 'Start Time')
etEarlyBird = Time(datetime.time(hour=18, minute=00), 'End Time')
mnuEarlyBird = Menu('Early Bird Dinner Menu', early_bird, stEarlyBird, etEarlyBird)

# create menu (Dinner)
dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
stDinner = Time(datetime.time(hour=17, minute=00), 'Start Time')
etDinner = Time(datetime.time(hour=23, minute=00), 'End Time')
mnuDinner = Menu('Dinner Menu', dinner, stDinner, etDinner)

# create menu (Kids)
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
stKids = Time(datetime.time(hour=11, minute=00), 'Start Time')
etKids = Time(datetime.time(hour=21, minute=00), 'End Time')
mnuKids = Menu('Kids Menu', kids, stKids, etKids)

# ------------------------------------
# CLASS: NAME
class Name():
    #constructor
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname
    #string representation
    def __repr__(self):
        return '{} {}'.format(self.first, self.last)
#TEST
p = Name('Dean', 'Jones')
p           #Dean Jones

# CLASS: ADDRESS INFO
class Address():
    #constructor
    def __init__(self, name='None', streetNo='None', streetName='None', quadrant='None', city='None', prov='None', postal='None'):
        self.name = name
        self.streetNo = streetNo
        self.streetName = streetName
        self.quadrant = quadrant
        self.city = city
        self.prov = prov
        self.postal = postal
    #string representation
    def __repr__(self):
        return '\n{}\n{} {} {}\n{}, {}\n{}'.format(self.name, self.streetNo, self.streetName, self.quadrant, self.city, self.prov, self.postal)
#TEST
#addr = Address('DEAN JONES', 16, 'WOODSTOCK RD', 'SW', 'Calgary', 'AB', 'T2W 5V8')
# addr = Address(Name('DEAN', 'JONES'), 16, 'WOODSTOCK RD', 'SW', 'Calgary', 'AB', 'T2W 5V8')
# addr.name.first         #'DEAN'
# addr.name.last          #'JONES'
addr = Address('Basta Fazoolin', 111, 'MAIN STREET', 'SE', 'Calgary', 'AB', 'X0X 0X0')

# CLASS: PHONE INFO
class Phone():
    #constructor
    def __init__(self, areaCode, digit3, digit4):
        self.areaCode = areaCode
        self.phone = '{}-{}'.format(digit3, digit4)
    #string representation
    def __repr__(self):
        return '({}) {}'.format(self.areaCode, self.phone)
#TEST
# ph = Phone(403, 555, 1234)
# ph              #(403) 555-1234

# CLASS: RESTAURANT INFO
class Restaurant():
    #constructor
    def __init__(self, address, phone, style):
        self.address = address
        self.phone = phone
        self.style = style
    #string representation
    def __repr__(self):
        return '\n{}\n{}\n\n{} Restaurant'.format(self.address, self.phone, self.style)
#TEST
r = Restaurant(Address('Basta Fazoolin', 111, 'MAIN STREET', 'SE', 'Calgary', 'AB', 'X0X 0X0'), Phone(403, 555, 1234), 'Family-Style Italian')
# Basta Fazoolin
# 111 MAIN STREET SE
# Calgary, AB
# X0X 0X0
# (403) 555-1234
#
# Family-Style Italian Restaurant


# CLASS: ITEM
class Item():
    #constructor
    def __init__(self, qty, item, price):
        self.qty = qty
        self.item = item
        self.price = price
        self.dict = {'qty': self.qty, 'item': self.item, 'price': self.price}
    #string representation
    def __repr__(self):
        return '{}'.format(self.dict)

#TEST
# itm1 = Item(2, 'cola', 1.00)
# itm2 = Item(1, 'fries', 2.00)
# itm3 = Item(1, 'burger', 5.00)
# itm1            #2, cola, 1.0
#CODE ACADEMY TEST (USE A MENU, to find items with correct price)
itm1 = Item(1, 'pancakes', mnuBrunch.items['pancakes'])
itm2 = Item(1, 'home fries', mnuBrunch.items['home fries'])
itm3 = Item(1, 'coffee', mnuBrunch.items['coffee'])
#'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
itm4 = Item(1, 'salumeria plate', mnuEarlyBird.items['salumeria plate'])
itm5 = Item(1, 'mushroom ravioli (vegan)', mnuEarlyBird.items['mushroom ravioli (vegan)'])
# 'salumeria plate': 8.00, 'pizza with quattro formaggi': 9.00, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,



# FUNCTION: currency format
def currency(num):
    return '${:,.2f}'.format(num)

# CLASS: ITEMS
class Items():
    #constructor
    def __init__(self, items_list):
        self.list = items_list
        #self.subtotal = self.subtotal()
        self.gst = 5.0                      #5.0% tax
        #self.tax = self.tax()
        #self.total = self.total()
    #string representation
    def __repr__(self):
        return '{}'.format(self.list)
    #print
    def print_items(self):
        print('Qty\t\tPrice\t\tDescription')
        for x in self.list:
            print('{}\t\t{}\t\t{}'.format(x['qty'], currency(x['price']), x['item'].title()))
    #string items
    def str_items(self):
        s = ''
        s += '\nQty\t\tPrice\t\tDescription'
        for x in self.list:
            s += '\n{}\t\t{}\t\t{}'.format(x['qty'], currency(x['price']), x['item'].title())
        return s
    #calculate subtotal (qty * price) for all items (sum)
    def subtotal(self):
        return sum([x['qty'] * x['price'] for x in self.list])
    #calculate tax
    def tax(self):
        return self.subtotal() * (5.0 / 100)
    #calculate TOTALS
    def total(self):
        return self.subtotal() + self.tax()

#TEST (ORDER)
i = Items([itm1.dict, itm2.dict, itm3.dict, itm4.dict, itm5.dict])
# i.print_items()
# qty     price   description
# 2       1.0     cola
# 1       2.0     fries
# 1       5.0     burger

# CLASS: BILL (RECEIPT)
class Bill():
    #constructor
    def __init__(self, restaurant, mnu, billNo, dateOfPurchase, itemsPurchased):
        self.restaurant = restaurant
        self.menu = mnu.name
        self.billNo = billNo
        self.date = dateOfPurchase
        self.itemsPurchased = itemsPurchased
    #string representation
    def __repr__(self):
        s = ''
        s += '\n-------------------------------------------------------'
        s += '\n{}'.format(self.menu)
        s += '\n{}{}\nBill#: {}\n\n{}'.format(self.date, self.restaurant, self.billNo, self.itemsPurchased.str_items())
        s += '\n'
        s += '\nSubTotal: {}'.format(currency(self.itemsPurchased.subtotal()))
        s += '\nTax @ {}%: {}'.format(self.itemsPurchased.gst, currency(self.itemsPurchased.tax()))
        s += '\nTotal: {}'.format(currency(self.itemsPurchased.total()))
        s += '\n-------------------------------------------------------'
        return s

#TEST
b = Bill(r, mnuBrunch, 101, Date(datetime.datetime.now()), i)
# -------------------------------------------------------
# Brunch Menu
# Thursday, Sep.06, 2018
#
# Basta Fazoolin
# 111 MAIN STREET SE
# Calgary, AB
# X0X 0X0
# (403) 555-1234
#
# Family-Style Italian Restaurant
# Bill#: 101
#
#
# Qty             Price           Description
# 1               $7.50           Pancakes
# 1               $4.50           Home Fries
# 1               $1.50           Coffee
#
# SubTotal: $13.50
# Tax @ 5.0%: $0.68
# Total: $14.18
# -------------------------------------------------------

# CLASS: FRANCHISE
class Franchise():
    #constructor
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    #string representation
    def __repr__(self):
        return '\n{}'.format(self.address)
    #string dump
    def str_dump(self):
        return '\naddress: {}\nmenu: {}'.format(self.address, self.menus)
    #list of available menus
    def available_menus(self, time):
        hr = time.hour24
        result = []
        for b in range(self.menus[0].start.hour24, self.menus[0].end.hour24):   #Brunch
            if b == hr:                                                         #if the (hour) is in (menu range)
                #result.append('b')                                              #add menu
                result.append(self.menus[0].name)
        for e in range(self.menus[1].start.hour24, self.menus[1].end.hour24):   #Early Bird (get range from start time to end time)
            if e == hr:                                                         #if the (hour) is in (menu range)
                #result.append('e')
                result.append(self.menus[1].name)   #add menu
        for d in range(self.menus[2].start.hour24, self.menus[2].end.hour24):   #Dinner
            if d == hr:                                                         #if the (hour) is in (menu range)
                #result.append('d')
                result.append(self.menus[2].name)                              #add menu
        for k in range(self.menus[3].start.hour24, self.menus[3].end.hour24):   #Kids
            if k == hr:                                                         #if the (hour) is in (menu range)
                #result.append('k')
                result.append(self.menus[3].name)                              #add menu
        return result


#TEST
#"12 East Mulberry Street"
addrFlag = Address('Basta Fazoolin', 12, 'East Mulberry Street', 'E', 'Calgary', 'AB', 'X0X 0X0')
mnuList = [mnuBrunch, mnuEarlyBird, mnuDinner, mnuKids]
flagship_store = Franchise(addrFlag, mnuList)
#"1232 West End Road"
new_installment = Franchise(Address('Basta Fazoolin', 1232, 'West End Road', 'W', 'Calgary', 'AB', 'X0X 0X0'), [mnuBrunch, mnuEarlyBird, mnuDinner, mnuKids])

#TEST (MENUS AVAILABLE)
t = Time(datetime.time(hour=13, minute=00), 'Menus available')
t1 = Time(datetime.time(hour=16, minute=00), 'Menus available')
t2 = Time(datetime.time(hour=18, minute=00), 'Menus available')
f = Franchise(addrFlag, mnuList)
f.available_menus(t)        #['b', 'k']
f.available_menus(t1)       #['e', 'k']
f.available_menus(t2)       #['d', 'k']
f.available_menus(t)        #['Brunch Menu', 'Kids Menu']
f.available_menus(t1)       #['Early Bird Dinner Menu', 'Kids Menu']
f.available_menus(t2)       #['Dinner Menu', 'Kids Menu']
#TEST (CODE ACADEMY)
test = Time(datetime.time(hour=12, minute=00), 'Menus available')
f.available_menus(test)     #['Brunch Menu', 'Kids Menu']
test2 = Time(datetime.time(hour=17, minute=00), 'Menus available')
f.available_menus(test2)    #['Early Bird Dinner Menu', 'Dinner Menu', 'Kids Menu']

# ----------------------
# CREATE A BUSINESS (Business --> Franchise --> Menu)
class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
#TEST
bus = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
#NEW MENU
arepas = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
stArepas = Time(datetime.time(hour=10, minute=00), 'Start Time')
etArepas = Time(datetime.time(hour=20, minute=00), 'End Time')
mnuArepas = Menu('Arepas Menu', arepas, stArepas, etArepas)
#MAKE FRANCHISE
#"189 Fitzgerald Avenue"
addrFlag2 = Address('Arepas Place', 189, 'Fitzgerald Avenue', 'None', 'Phoenix', 'AZ', '67760')
mnuList2 = [mnuArepas]
arepas_place = Franchise(addrFlag2, mnuList2)
# type(arepas_place)            #<class '__main__.Franchise'>
#MAKE A BUSINESS
bus2 = Business("Take a' Arepa", [arepas_place])
# type(bus2)                    #<class '__main__.Business'>
