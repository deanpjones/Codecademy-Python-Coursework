letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#learner code here:
letters_to_points = {key:value for key, value in zip(letters,points)}
letters_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letters_to_points:
    	point_total += letters_to_points[letter]
  return point_total

brownie_points = score_word("Brownie")
print(brownie_points)

players_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in players_to_words.items():
  score = 0
  for word in words:
    score += score_word(word)
  player_to_points[player] = score

print(player_to_points)
