# SCRABBLE
# PROJECT #10
# CODE ACADEMY
# PROGRAMMING WITH PYTHON
# Dean Jones, Aug.26, 2018

# In this project, you will process some data from a group of friends playing scrabble.
# You will use dictionaries to organize players, words, and points.
#
# There are many ways you can extend this project on your own if you finish and want to get more practice!

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

#create dictionary (letter: points)
letter_to_points = {k:v for k,v in zip(letters, points)}

#FUNCTION: GET VALUE OF WORD
def word_value(word):
  return [letter_to_points[x] for x in word.upper()]
#FUNCTION: SCORE A WORD
def score_word(word):
  return sum(word_value(word))
#TEST
brownie_points = score_words('BROWNIE') #15

#FUNCTION: SUM LIST OF WORDS
def list_points(my_list):
  return [score_word(x) for x in my_list]
#TEST
list_points(['BLUE','TENNIS','EXIT'])
#[6, 12, 11]
#FUNCTION: SUM LIST POINTS
def sum_list_points(my_list_pts):
  return sum(list_points(my_list_pts))
#TEST
sum_list_points(['BLUE','TENNIS','EXIT'])
#29, sum of [6, 12, 11]

#create dictionary (players words)
player_to_words = {'player1': ['BLUE',	'TENNIS',	'EXIT'],	'wordNerd': ['EARTH', 'EYES',	'MACHINE'],	'Lexi Con': ['ERASER', 'BELLY',	'HUSKY'],	'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

#empty dictionary (player points)
player_to_points_list = {}
#FUNCTION: PLAYER POINTS LIST
def player_pt_list():
  global player_to_words
  global player_to_points_list
  for k,v in player_to_words.items():
    player_to_points_list[k] = list_points(v)
  return player_to_points_list
#{'player1': [6, 12, 11], 'wordNerd': [8, 7, 17], 'Lexi Con': [6, 10, 15], 'Prof Reader': [14, 8, 9]}

#FUNCTION: PLAYER SUM (POINTS LIST)
player_to_points = {}
def player_totals():
  global player_to_words
  global player_to_points_list
  for k,v in player_to_words.items():
    player_to_points[k] = sum_list_points(v)
  return player_to_points
#{'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

#FURTHER PRACTISE...
#FUNCITON: PLAY WORD
#a function that would take in a player and a word, and add that word to the list of words they've played
def play_word(player, word):
  player_to_words[player].append(word)
  return word + ' added'
#TEST
play_word('player1', 'Muppet')		#'Muppet added'
player_to_words['player1']				#['BLUE', 'TENNIS', 'EXIT', 'Muppet']
#FUNCTION: REMOVE WORD
def remove_word(player, word):
  player_to_words[player].remove(word)
  return word + ' removed'
#TEST
remove_word('player1', 'Muppet')	#'Muppet removed'
player_to_words['player1']				#['BLUE', 'TENNIS', 'EXIT']

  
