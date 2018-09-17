# ABRUPTLY GOBLINS (ROLE PLAYING GAME)
# PROJECT #11
# CODE ACADEMY
# PROGRAMMING WITH PYTHON
# Dean Jones, Aug.28, 2018

# ------------------------------------------------------------------------
# Introduction
# Opening your comic book store, the Sorcery Society, has been a lifelong dream come true.
# You quickly diversified your shop offerings to include miniatures, plush toys, collectible card games,
# and board games. Eventually, the store became more a games store with a selection of this week's newest
# comic books and a small offering of graphic novel paperbacks. Completing your transformation means offering
# space for local tabletop gamers. They love to play their favorite RPG, "Abruptly Goblins!" and will happily
# pay you per chair to secure the space to do it. Unfortunately, planning the game night has fallen to you.
# If you pick the wrong night, not enough people will come and the game night will be cancelled. You decide
# it's best that you automate the game night selector to get the most people through the door. First you
# need to create a list of people who will be attending the game night.
# ------------------------------------------------------------------------
# Instructions
# Create an empty list called gamers. This will be your list of people who are attending game night.
# PEOPLE ATTENDING (GAME NIGHT)
gamers = []

# Now we want to create a function that will update this list and add a new gamer to the this gamers list.
# Each gamer should be a dictionary with the following keys:
#   "name":             a string that contains the gamer's full or presumed name. E.g., "Vicky Very"
#   "availability":     a list of strings containing the names of the days of the week that the gamer is available. E.g., ["Monday", "Thursday", "Sunday"]
# Instructions
# Create a function called add_gamer that takes two parameters: gamer and gamers_list.
# The function should check that the argument passed to the gamer parameter has both
# "name" and a "availability" as keys and if so add gamer to gamers_list.

#UPDATE (person info)

#CREATE (ADD person)
#FUNCTION: KEY-VALUE ({name: availability})
def add_gamer(_name, _availability):
    if [x for x in gamers if x['name'] == _name] == []:                 #check to make sure (name hasn't been added yet)
        gamers.append({'name': _name, 'availability': _availability})
        return gamers
    else:
        return _name + " has already been added."

#TEST
# Dean, (I can only make in WEEKENDS ONLY)
add_gamer('Dean', get_days(65))                 #[{'name': 'Dean', 'availability': ['Sunday', 'Saturday']}]
# Nadine, (I work weekends so I can go WEEKDAYS ONLY)
add_gamer('Nadine', get_days(62))               #[{'name': 'Nadine', 'availability': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}]
add_gamer('Kimberly Warner', get_days(38))      #[{'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}]

#------------------------------------
#------------------------------------
#RESET
#ADD A BUNCH...
reset(gamers)   #reset (to start)
# add Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays
add_gamer('Kimberly Warner', get_days(38))

#{"Sunday": 1, "Monday": 2, "Tuesday": 4, "Wednesday": 8, "Thursday": 16, "Friday": 32, "Saturday": 64}
add_gamer('Thomas Nelson', get_days(84))
#get_days_num(["Tuesday", "Thursday", "Saturday"])                 returns 84
# add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer('Joyce Sellers', get_days(106))
#get_days_num(["Monday", "Wednesday", "Friday", "Saturday"])        returns 106
# add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer('Michelle Reyes', get_days(25))
#get_days_num(["Wednesday", "Thursday", "Sunday"])                  returns 25
# add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer('Stephen Adams', get_days(80))
#get_days_num(["Thursday", "Saturday"])                             returns 80
# add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer('Joanne Lynn', get_days(18))
# get_days_num(["Monday", "Thursday"])                              returns 18
# add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer('Latasha Bryan', get_days(3))
# get_days_num(["Monday", "Sunday"])                                returns 3
# add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer('Crystal Brewer', get_days(112))
#get_days_num(["Thursday", "Friday", "Saturday"])                   returns 112
# add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer('James Barnes Jr.', get_days(29))
#get_days_num(["Tuesday", "Wednesday", "Thursday", "Sunday"])       returns 29
# add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer('Michel Trujillo', get_days(14))
#get_days_num(["Monday", "Tuesday", "Wednesday"])                   returns 14
# add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
#------------------------------------
#------------------------------------

#***********************************************
#STATUS CODES {code: [code, name, description]}
ERR = {'001': ['001', 'NO_INDEX', 'Bad name, no index'], '002': ['002', 'NAME_NOT_FOUND', 'The name search did not find that user in the dictionary.']}
#***********************************************

#READ (GET INFO FOR INDEX)
def get_person(_name):
    person = [x for x in gamers if x['name'] == _name]
    if person != []:
        return person
    else:
        return ERR['002']

#READ (GET INDEX of person)
def get_index(_name):
    try:
        i = gamers.index([x for x in gamers if x['name'] == _name][0])
    except:
        return ERR['001']
    return i

#DELETE (REMOVE one person)
def del_gamer(_name):
    i = get_index(_name)
    if isinstance(i, int):      #test returns an isinstance
        gamers.pop(i)           #remove from list
        return _name + ' was removed.'
    else:
        return _name + ' was NOT removed.'
#TEST
del_gamer('Dean')       #'Dean was removed.'
del_gamer('Nadine')     #'Nadine was removed.'
# can't remove twice
del_gamer('Nadine')     #'Nadine was NOT removed.'

#DELETE (reset master list)
#RESET
def reset(my_list):
    my_list.clear()
    return my_list

#FUNCTION: GET NUMBER (FOR LIST OF DAYS)
def get_days_num(my_list):
    # days of week (dictionary)
    days_of_week = {"Sunday": 1, "Monday": 2, "Tuesday": 4, "Wednesday": 8, "Thursday": 16, "Friday": 32, "Saturday": 64}
    return sum([v for k,v in days_of_week.items() for y in my_list if y == k])

#FUNCTION: GET (LIST OF) DAYS
# num = saves a ONE NUMBER (for a LIST of)(days of week, to index)
# num = sum of list of indexes [1, 4] --> sums to 5
# this is an very efficient way of storing a list of values (as an integer)
def get_days(num):
    # days of week (dictionary)
    days_of_week = {"Sunday": 1, "Monday": 2, "Tuesday": 4, "Wednesday": 8, "Thursday": 16, "Friday": 32, "Saturday": 64}
    return [k for k,v in days_of_week.items() for y in sum_powers2(num) if y == v]
#TEST
# num = 5 ([1,4] --> ['Sunday', 'Tuesday'])
get_days(5)         #['Sunday', 'Tuesday']
get_days(7)         #['Sunday', 'Monday', 'Tuesday']
# weekend only [1, 64]
get_days(65)        #['Sunday', 'Saturday']
# weekdays only [2,4,8,16,32]
get_days(62)        #['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# print all
for x in range(128):
    print(get_days(x))
# []
# ['Sunday']
# ['Monday']
# ['Sunday', 'Monday']
# ['Tuesday']
# ['Sunday', 'Tuesday']
# ['Monday', 'Tuesday']
# ['Sunday', 'Monday', 'Tuesday']
# ...
# ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#FUNCTION: LIST OF POWERS (SUM NUMBER)
# creates a LIST of POWERS OF TWO (that SUM to the NUMBER)
def sum_powers2(num):
    temp = num      #temp number
    pick = 0
    result = []
    # powers of 2
    my_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #loop through list
    while (temp != 0):
        # max num without going over
        pick = max([x for x in my_list if x <= temp])
        result.append(pick)     #add to list
        temp = temp - pick      #counter (also LIST value)
    result.sort()               #doesn't return value
    return result
#TEST
sum_powers2(5)      #[1, 4]
sum_powers2(7)      #[1, 2, 4]
sum_powers2(16)     #[16]
sum_powers2(127)    #[1, 2, 4, 8, 16, 32, 64]

#-----------------------
# Finding the perfect availability
# Now that we have a list of all of the people interested in game night, we want to be able to calculate which nights
# would have the most participation. First we need to create a frequency table which correlates each day of the week with gamer availability.
#
# Instructions
# Create a function called build_daily_frequency_table that takes no argument returns a dictionary with the days of the week as keys and 0s
# for values. We'll be using this to count the availability per night. Call build_daily_frequency_table and save the results to a variable
# called count_availability.

#FUNCTION: DAILY FREQUENCY TABLE (counts the days of week picked)
# no arguments
# returns dictionary
def build_daily_frequency_table():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    table = {}
    for d in days:
        count = len([y for x in gamers for y in x['availability'] if y == d])
        table[d] = count
    return table
#TEST
table = build_daily_frequency_table()
#{'Sunday': 3, 'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4}

#FUNCTION: FIND BEST NIGHT
# return LIST of MAX TOTALS (in case there is more than one night)
# t = table
def find_best_night(t):
    most_days_picked = max([v for k,v in t.items()])                #returns 6
    return [k for k,v in t.items() if v == most_days_picked]        #['Thursday', 'Saturday']

#TEST
best_night = find_best_night(table)              #['Thursday'] because (6 people) picked it (it was highest)
# test for (two nights with same max total)
table2 = {'Sunday': 3, 'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 6}
find_best_night(table2)             #['Thursday', 'Saturday']

#-----------------------------------------
# And let's make a list of all of the people who are available that night.
#
# Instructions
# Create a function available_on_night that takes two parameters: gamers_list and day and returns a list of people
# who are available on that particular day.
# Call available_on_night with gamers and game_night and save the result into the variable attending_game_night.
# Print attending_game_night.

#FUNCTION: GET LIST OF PEOPLE (AVAILABLE ON BEST NIGHT)
def available_on_night(gamers_list, best_night):
    result = {}
    for d in best_night:
        people_available = [x['name'] for x in gamers_list for d in best_night if d in x['availability']]
        result[d] = people_available
    return result
#TEST
people_available = available_on_night(gamers, best_night)
#{'Thursday': ['Thomas Nelson', 'Michelle Reyes', 'Stephen Adams', 'Joanne Lynn', 'Crystal Brewer', 'James Barnes Jr.']}
#-----------------------------------------
# Generating an E-mail for the Participants
# With the best day for Abruptly Goblins! determined with computer precision, we need to let the attendees know that the game night
# is on a night they can attend. Let's start by creating a form email to send to each of the participants that we'll fill out with data later.
#
# Instructions
# Define a string, called form_email with interpolation variables {name}, {day_of_week}, and {game} (in case we decide we want to use this
# featureset to host a different game night). Use it to tell your gaming attendees the night their Abruptly Goblins! game can be played.

#EMAIL FORMAT
def send_email(_people_available, _game):
    #email template
    form_email = '''
    ------------
    Dear {name},
    We are hosting {game}, on {day_of_week} of next week. Please RSVP if you can attend.

    Regards,
    Dean Jones
    '''
    for k,v in _people_available.items():
        for n in v:
            print(form_email.format(name = n, day_of_week = k, game = _game))
#TEST
send_email(people_available, 'Abruptly Goblins')
    # ------------
    # Dear James Barnes Jr.,
    # We are hosting Abruptly Goblins, on Thursday of next week. Please RSVP if you can attend.
    #
    # Regards,
    # Dean Jones
#-----------------------------------------------------
# Afterward
# You feel bad for the folks who weren't able to attend on the decided upon game night, and try to use your currently
# written methods to have a second game night of the week.
#
# Instructions
# Create a list unable_to_attend_best_night of everyone in gamers that wasn't able to attend game night on game_night.
# Create second_night_availability frequency table by calling build_daily_frequency_table.
# Call calculate_availability with unable_to_attend_best_night and second_night_availability.
# Call find_best_night with the now filled-in second_night_availability, save the results in second_night.

#FUNCTION: GET ALL OTHER PEOPLE (THAT WEREN'T AVAILABLE)
def not_available(gamers_list, best_night):
    all_people = [x['name'] for x in gamers_list]       #get all people (who are signed up)
    p_avail = people_available[best_night]              #get (people available)
    return list(set(all_people) - set(p_avail))         #get the (difference) between two lists
#TEST
second_people = not_available(gamers, 'Thursday')
#['Joyce Sellers', 'Kimberly Warner', 'Latasha Bryan', 'Michel Trujillo']

#FUNCTION: GET SECOND HIGHEST (IN LIST)
def second_highest(l):
    return list(set(l))[-2]

#FUNCTION: FIND (SECOND BEST) NIGHT
# t = table
def find_seconde_best_night(t):
    second_most_days_picked = second_highest([v for k,v in t.items()])      #returns 5
    return [k for k,v in t.items() if v == second_most_days_picked]         #['Monday']
    #should get 'Monday' as second highest
    #table --> {'Sunday': 3, 'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4}
#TEST
second_night = find_seconde_best_night(table)      #['Monday']

#CREATE DICTIONARY (for secondary people)
second = {}
second[second_night[0]] = second_people

#SEND EMAIL TO REMAINING PEOPLE...
#EMAIL FORMAT
def send_email2(_second_people, _game):
    #email template
    form_email = '''
    ------------
    Dear {name},
    We are hosting {game} for a SECOND NIGHT, on {day_of_week} of next week. Please RSVP if you can attend.

    Regards,
    Dean Jones
    '''
    for k,v in _second_people.items():
        for n in v:
            print(form_email.format(name = n, day_of_week = k, game = _game))
#TEST
send_email2(second, 'Abruptly Goblins')
    # ------------
    # Dear Joyce Sellers,
    # We are hosting Abruptly Goblins for a SECOND NIGHT, on Monday of next week. Please RSVP if you can attend.
    #
    # Regards,
    # Dean Jones
    #
    #
    # ------------
    # Dear Kimberly Warner,
    # We are hosting Abruptly Goblins for a SECOND NIGHT, on Monday of next week. Please RSVP if you can attend.
    #
    # Regards,
    # Dean Jones
    #
    #
    # ------------
    # Dear Latasha Bryan,
    # We are hosting Abruptly Goblins for a SECOND NIGHT, on Monday of next week. Please RSVP if you can attend.
    #
    # Regards,
    # Dean Jones
    #
    #
    # ------------
    # Dear Michel Trujillo,
    # We are hosting Abruptly Goblins for a SECOND NIGHT, on Monday of next week. Please RSVP if you can attend.
    #
    # Regards,
    # Dean Jones
