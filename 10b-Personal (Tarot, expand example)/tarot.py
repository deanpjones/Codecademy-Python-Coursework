#TAROT
#DEAN JONES, AUG. 22, 2018
#HAVE FUN (see what I can make here... :)

#TODO
# got a random SPREAD1 working
# add USER PICK functionality
# explore (the random) using milliseconds, vs other means to get RANDOM NUMBER for (past, present, future)?
# ADD OBJECT (for CARDS)
# add CARD DESCRIPTIONS (magician, where to add info?)(how much can I add?)
# add USER QUESTIONS, before they pull card...

#full deck
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
#create (temporary deck to remove from...)
play = tarot.copy()         #copy deck
#card picks
picks = []
#spread (cards pulled)
spread = {}     #empty dictionary

#FUNCTION: RESET DECK
def reset():
    global play                 #need to reference global variable
    play = tarot.copy()         #copy deck
    return "Deck reset"

#FUNCTION: PULL CARD (remove from deck)
def pull(card_key):
    return play.pop(card_key, 'Card not found')

#FUNCTION: RANDOM NUMBER GENERATOR (DEAN :)
def random():
    #use DATE in milliseconds to get random number (between 1 and 22)
    import datetime
    d = datetime.datetime.now()
    ms = d.microsecond
    #get (tenths and hundredths)
    ms1 = ms // 10000
    #do mod (modular 22) to get value (card to pick)
    #random = (ms1 % 21) + 1         #can't be zero (add one)
    return ms1

#FUNCTION: RANDOM3 (TAKE THREE NUMBERS)(ALL FROM microsecond)
def random3():
    import datetime
    d = datetime.datetime.now()
    ms = d.microsecond              #179741
    str_ms = str(ms)
    #chop milliseconds (into 3 parts) [17, 97, 41]
    return [int(str_ms[0:2]), int(str_ms[2:4]), int(str_ms[4:6])]

#FUNCTION: PICK A CARD (can't pick same card twice)
# pick takes (random) and uses that to select (first card), then list shrinks, only leaving what's available left (just like in real life)
# pk = random2()
def pick_three_cards(pk):
    global picks        #global picks
    picks = []          #reset
    #get range
    t = list(range(1, 23))
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]    #this represents (22 major arcana cards)
    #card 1
    p0 = pk[0] % len(t)
    picks.append(t.pop(p0))         #pick card (and remove)(*** deck keeps getting smaller, after each pick ***)
    #card 2
    p1 = pk[1] % len(t)
    picks.append(t.pop(p1))         #pick card (and remove)
    #card 3
    p2 = pk[2] % len(t)
    picks.append(t.pop(p2))         #pick card (and remove)
    return [picks, t]

#TEST
pick_three_cards(random3())
#[[15, 5, 3], [1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22]]
pick_three_cards(random3())
#[[9, 10, 15], [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22]]


#SPREAD-1 (past, present, future) cards
def spread1():
    p = pick_three_cards(random3())
    spread['past'] = tarot[p[0][0]]
    spread['present'] = tarot[p[0][1]]
    spread['future'] = tarot[p[0][2]]
    return spread
