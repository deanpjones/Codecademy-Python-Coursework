# CODED CORRESPONDENCE
# PROJECT #9
# CODE ACADEMY
# PROGRAMMING WITH PYTHON
# Dean Jones, Sep.5, 2018
# My own personal attempt at creating a VIGENERE CIPHER (that is more complex)

# IDEA
# The VIGENERE CIPHER is based on indexing a 2D ARRAY KEY (using a keyword)
# (I am Dean)(Anagram)(Idea man)
# My IDEA is to CREATE (a key) of the (2D ARRAY)
#   -there are 26! (403 million billion billions) permutations (just different a-z combinations)
#   -if I (SCRAMBLE) the KEY AS WELL (same way as scrambling VBM grids)(then it will make it increasingly harder to crack)
#   -so the TWO PEOPLE would already need the KEY (CODE) as well as now a (KEYWORD)
#   -could also use a (keyword) as an (anagram) to confuse it one further
#   -ADD SPACE (to the CIPHER) this would in essence (make the WORDS appear DIFFERENT LENGTHS then they actually are?)
#       -this would be good to TEST on a regular CIPHER (CAESAR CIPHER)


#NEW IDEAS (CIPHERS)
#CAESAR SHIFT (but add a SPACE)(*** this will CONFUSE decryption because the LENGTH OF WORDS WILL CHANGE ***)
# SPACES (are normally just ignored, WHAT IF IT WAS PART OF ENCRYPTION :)
# eg. key = ["de fghijklmnopqrstuvwxyzabc"]     //replace somewhere common ('e', 'a', 'I'? ...test a few)

# CRYPTOGRAPHY CIPHER
# In this project, you will be working to code and decode various messages between you and your fictional cryptography
# enthusiast pen pal Vishal. You and Vishal have been exchanging letters for quite some time now and have started to
# provide a puzzle in each one of your letters. Here is his most recent letter:

# -----------------------------------------------------------------------------------------------------------------------
# Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher.
# Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset.
# For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to
# the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l".
# Then I have my coded message,"ebiil"! Now I can send you my message and the offset and you can decode it. The best thing is
# that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going
# to send you a longer coded message that you have to decode yourself!

# CIPHER...
# xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

# This message has an offset of 10. Can you decode it?
# -----------------------------------------------------------------------------------------------------------------------

letters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_lowercase = "abcdefghijklmnopqrstuvwxyz"

#FUNCTION: CAESAR CIPHER (SPACE IN MIDDLE OF LETTERS)
def create_cipher(shift_n):
    #alphab = 'abcdefghijklmnop qrstuvwxyz'
    alphab = 'abcdefghijklmnopqr stuvwxyz'
    cipher = alphab[shift_n:] + alphab[:shift_n]
    return cipher

#TEST
create_cipher(2)
'cdefghijklmnop qrstuvwxyzab'

#FUNCTION: ENCODE OR DECODE
# code = 'encode' or 'decode'
def encode_decode(my_string, shift_n, code):
    result = ''
    #alphab = 'abcdefghijklmnopqrstuvwxyz,\' !?.'
    alphab = 'abcdefghijklmnop qrstuvwxyz'
    cipher = create_cipher(shift_n)
    #cipher = create_cipher('right', 10)
    if code == 'encode':
        for x in my_string:
            #print(result)
            #print(alphab)
            #print(alphab.index(x))
            result = result + cipher[alphab.index(x)]      #get (cipher) letter index
    elif code == 'decode':
        for x in my_string:
            result = result + alphab[cipher.index(x)]      #get (alphabet) letter index
    else:
        return 'Something went wrong, make sure use ("encode or decode") for first argument'
    return result

#TEST
encode_decode('hey there', 10, 'encode')        #'qoizdqobo' *** NOTE, there are no spaces, so this would be confusing to think of deciphering ***
encode_decode('qoizdqobo', 10, 'decode')        #'hey there'
#TEST2
s = 'this is my first attempt at making a new caesar cipher'        # NOTE, the STRING (needs to all be lowercase) at the moment
encode_decode(s, 10, 'encode')
'dqrczrczvizprbcdzkddovydzkdzvktrw zkzwogzmkockbzmryqob'
s_encrypted = 'dqrczrczvizprbcdzkddovydzkdzvktrw zkzwogzmkockbzmryqob'
encode_decode(s_encrypted, 10, 'decode')        #'this is my first attempt at making a new caesar cipher'
#TEST3 (changed the KEY)(alphab = 'abcdefghijklmnopqr stuvwxyz')
encode_decode(s, 10, 'encode')
# 'dr cz czvizp bcdzkddovydzkdzvkt wqzkzwogzmkockbzm yrob'
se = 'dr cz czvizp bcdzkddovydzkdzvkt wqzkzwogzmkockbzm yrob'
encode_decode(se, 10, 'decode')
# 'this is my first attempt at making a new caesar cipher'






# TODO, redo VIGENERE CIPHER... below.













#STEP 3
#TWO MORE MESSAGES...
# Vishal sent over another reply, this time with two coded messages!
# You're getting the hang of this! Okay here are two more messages, the first one is coded just like before
# with  an offset of ten, and it contains the hint for decoding the second message!

t1 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
t2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
encode_decode(t1, 'right', 10, 'decode')
# 'the offset for the second message is fourteen.'
encode_decode(t2, 'right', 14, 'decode')
# 'performing multiple caesar ciphers to code your messages is even more secure!'


#STEP 4
# Solving a Caesar Cipher without knowing the shift value
# To test your cryptography skills, this next coded message is going to be harder than the last couple to crack.
# It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of   the shift.
# You'll have to (brute force) it yourself.

t3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
#figure out range to test (brute force)
alph = create_cipher('right', 10)
len(alph)           #returns 32 (test range 0 to 32)
for x in range(32):
    print("x: ", x, "message: ", encode_decode(t3, 'right', x, 'decode'))
    #... check all messages to find one that is READABLE
    #THE SHIFT ON 7 (is readable)
#test (shift of 7) to check message
encode_decode(t3, 'right', 7, 'decode')
# "computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to keep our messages safe."

#STEP 5
# THE VIGENERE CIPHER
# Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy,
# and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to
# teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century,
# but named after another cryptologist from the 16th century, Blaise de Vigenère.

# The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher.
# What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each
# individual letter. The value of the shift for each letter is determined by a given keyword.

#CAESAR CIPHER, is using a SHIFT (for ALL LETTERS)
#VIGENERE CIPHER, is using a KEYWORD
# TODO... need to read and understand this cypher first ...(looks like the one they used in GOVERNMENT OF CANADA CIPHER)

# THREE PARTS (message, keyword, difference_in_place)
# ------------------------------------------------------------------------------
# message:                          b  a  r  r  y  i  s  t  h  e  s  p  y

# keyword phrase:                   d  o  g  d  o  g  d  o  g  d  o  g  d

# difference in place value:        2  14 15 12 16 24 11 21 25 22 22 17 5
# ------------------------------------------------------------------------------
# the KEYWORD is repeated the LENGTH OF THE MESSAGE (each letter matches for key)
# the way this works... (count from MESSAGE to the LETTER IN KEYWORD)
#               1 2 3 4 5 6 7 8 9
# ALPHABET      a b c d e f g h i
#               j k l m n o p q r
#               s t u v w x y z

# examples, b --> d (2 places), a --> o (14 places), r --> g (15 places), r --> d (12 places)
# WARNING, there was some ERRORS in the INSTRUCTIONS on Jupyter, which made this VERY CONFUSING...

# SEE LINK (for a great clarification)
# http://crypto.interactive-maths.com/vigenegravere-cipher.html
#
# BUILD KEY (VIGENERE CIPHER KEY)
# use loop to create (cipher text)
for x in range(26):
    create_cipher('left', x)

# "abcdefghijklmnopqrstuvwxyz,' !?."
# "bcdefghijklmnopqrstuvwxyza,' !?."
# "cdefghijklmnopqrstuvwxyzab,' !?."
# ...


# vigenere_key[0][2]            #returns 'c'
# vigenere_key[1][2]            #returns 'd'
# SYNTAX, vigenere_key[row][column], vigenere_key[message][key]

# FUNCTION: GET INDEX (OF LETTER)
def get_index(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.index(letter)

# VIGENERE CIPHER KEY
vigenere_key_OLD = [
"abcdefghijklmnopqrstuvwxyz,' !?.",
"bcdefghijklmnopqrstuvwxyza,' !?.",
"cdefghijklmnopqrstuvwxyzab,' !?.",
"defghijklmnopqrstuvwxyzabc,' !?.",
"efghijklmnopqrstuvwxyzabcd,' !?.",
"fghijklmnopqrstuvwxyzabcde,' !?.",
"ghijklmnopqrstuvwxyzabcdef,' !?.",
"hijklmnopqrstuvwxyzabcdefg,' !?.",
"ijklmnopqrstuvwxyzabcdefgh,' !?.",
"jklmnopqrstuvwxyzabcdefghi,' !?.",
"klmnopqrstuvwxyzabcdefghij,' !?.",
"lmnopqrstuvwxyzabcdefghijk,' !?.",
"mnopqrstuvwxyzabcdefghijkl,' !?.",
"nopqrstuvwxyzabcdefghijklm,' !?.",
"opqrstuvwxyzabcdefghijklmn,' !?.",
"pqrstuvwxyzabcdefghijklmno,' !?.",
"qrstuvwxyzabcdefghijklmnop,' !?.",
"rstuvwxyzabcdefghijklmnopq,' !?.",
"stuvwxyzabcdefghijklmnopqr,' !?.",
"tuvwxyzabcdefghijklmnopqrs,' !?.",
"uvwxyzabcdefghijklmnopqrst,' !?.",
"vwxyzabcdefghijklmnopqrstu,' !?.",
"wxyzabcdefghijklmnopqrstuv,' !?.",
"xyzabcdefghijklmnopqrstuvw,' !?.",
"yzabcdefghijklmnopqrstuvwx,' !?.",
"zabcdefghijklmnopqrstuvwxy,' !?.",
]
vigenere_key = [
"abcdefghijklmnopqrstuvwxyz",
"bcdefghijklmnopqrstuvwxyza",
"cdefghijklmnopqrstuvwxyzab",
"defghijklmnopqrstuvwxyzabc",
"efghijklmnopqrstuvwxyzabcd",
"fghijklmnopqrstuvwxyzabcde",
"ghijklmnopqrstuvwxyzabcdef",
"hijklmnopqrstuvwxyzabcdefg",
"ijklmnopqrstuvwxyzabcdefgh",
"jklmnopqrstuvwxyzabcdefghi",
"klmnopqrstuvwxyzabcdefghij",
"lmnopqrstuvwxyzabcdefghijk",
"mnopqrstuvwxyzabcdefghijkl",
"nopqrstuvwxyzabcdefghijklm",
"opqrstuvwxyzabcdefghijklmn",
"pqrstuvwxyzabcdefghijklmno",
"qrstuvwxyzabcdefghijklmnop",
"rstuvwxyzabcdefghijklmnopq",
"stuvwxyzabcdefghijklmnopqr",
"tuvwxyzabcdefghijklmnopqrs",
"uvwxyzabcdefghijklmnopqrst",
"vwxyzabcdefghijklmnopqrstu",
"wxyzabcdefghijklmnopqrstuv",
"xyzabcdefghijklmnopqrstuvw",
"yzabcdefghijklmnopqrstuvwx",
"zabcdefghijklmnopqrstuvwxy",
]

# FUNCTION: ENCODE LETTER (VIGENERE CIPHER)
def encode_letter_vigenere(message_letter, key_letter):
    return vigenere_key[get_index(message_letter)][get_index(key_letter)]

#TEST       http://crypto.interactive-maths.com/vigenegravere-cipher.html
encode_letter_vigenere('b', 'a')        #'b'
encode_letter_vigenere('a', 'b')        #'b'
encode_letter_vigenere('s', 'a')        #'s'
encode_letter_vigenere('i', 't')        #'b'
encode_letter_vigenere('t', 'g')        #'z'
encode_letter_vigenere('h', 'i')        #'p'

# trying to match (key = 't', cipher = 'b', messsge = 'i')
# key = vigenere_key[0][19] = 't'
# cipher = vigenere_key[?][19] == 'b' --> row 8 (or 8th row index)
# message = vigenere_key[8][0] = 'i'

#FUNCTION: ADD SPACES
def add_spaces(message, key_string):
    result = key_string
    spaces_indexes = find_all(message, ' ')     #[1, 4]
    #convert list (increment each place)(*** need to do this as I iterate to put in correct placeholder ***)
    #v = [x + y for (x, y) in zip(spaces_indexes, range(len(spaces_indexes)))]   #returns [1, 5] adds [0, 1, 2, 3, ...] to LIST
    #add spaces to all indexes
    #for index in v:
    for index in spaces_indexes:
        result = insert_char(result, ' ', index)
    return result
#TEST
add_spaces('I am Dean', 'dogdogdog')            #'d ogd ogdog'

#FUNCTION: KEY STRING (build key_string same length as message)
def (message, key, code='no_spaces'):
    #*** NOTE, I think this is INCORRECT, the letters were not encoded properly on Code Academy ***
    #code = 'add_spaces'                                #USE THIS TO ADD SPACES...
    #code = 'no_spaces'
    result = ''
    #print(result)
    result = key * ((len(message) // len(key)) + 1)     #get quotient (then add one)(multiply string that many times)
    #print(result)
    #add spaces (if necessary?)
    if code == 'add_spaces':
        result = add_spaces(message, result)
    #print("spaces: ", result)
    #crop off the string (the same length of the message)
    result = result[:len(message)]
    #print("crop: ", result)
    return result

#**********************************************************************
#**********************************************************************
#FUNCTION: DECODE LETTER (VIGENERE CIPHER)
def decode_letter_vigenere(key_letter, cipher_letter):
    message_letter = '_'     #return '_' if there isn't no cipher (like spaces, or punctuation)
    #,' !?.
    # if cipher_letter == ',':
    #     message_letter = ','
    # elif cipher_letter == "'":
    #     message_letter = "'"
    # elif cipher_letter == ' ':
    #     message_letter = ' '
    # elif cipher_letter == '!':
    #     message_letter = '!'
    # elif cipher_letter == '?':
    #     message_letter = '?'
    # elif cipher_letter == '.':
    #     message_letter = '.'
    if cipher_letter == ',' or cipher_letter == "'" or cipher_letter == ' ' or cipher_letter == '!' or cipher_letter == '?' or cipher_letter == '.' or cipher_letter == '_':
        message_letter = cipher_letter                                 #return ' ' (SPACE), if get a ' ' (SPACE)
    else:
        try:
            #get KEY INDEX
            key_index = vigenere_key[0].index(key_letter)
            #key_index = vigenere_key[0].index('t')                     #returns 19
            #Which ROW has (cipher_letter at key_index)?
            cipher_row = vigenere_key[key_index].index(cipher_letter)   #seems a bit weird how I do this but it will work ;)
            #cipher_row = vigenere_key[key_index].index('b')            #returns 8 (row 8)
            #get first letter of this row (this is your result!)
            message_letter = vigenere_key[cipher_row][0]
        except ValueError as e:
            print("ValueError: ", e)
    return message_letter

#TEST
decode_letter_vigenere('t', 'b')                #returns 'i'

#FUNCTION: DECODE MESSAGE (VIGENERE CIPHER)
def decode_vigenere(cipher_message, key, code):
    result = ''
    #print("cipher_message: ", cipher_message)
    #print("len cipher_message: ", len(cipher_message))
    #print("key: ", key)
    key_string = get_key_string(cipher_message, key, code)               #'d ogd ogdog'
    #print("len key_string: ", len(key_string))
    #print("key_string: ", key_string)
    #
    #STRING LIST
    result_list = [decode_letter_vigenere(k, c) for (k, c) in zip(key_string, cipher_message)]
    result = ''.join(result_list)
    return result

decode_vigenere("B SBFXDX EYAFITW".lower(), 'battista', 'add_spaces')   #'a simple example'
decode_vigenere('dfc jhjj ifyh', 'friends', 'no_spaces')                #'you were able...'
#NOTE, tested... the CODE ACADEMY (CIPHER) is USING THE (KEY) in the (SPACES) (...need to ADJUST KEY...)
#**********************************************************************
#**********************************************************************
#TEST
message = 'dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!'
key = 'friends'
decode_vigenere(message, key, 'no_spaces')
#'you were able to decode this? nice work! you are becoming quite the expert at crytography!'
#TEST 2   http://crypto.interactive-maths.com/vigenegravere-cipher.html
message2 = 'ETGU RLXRGA JGM, OMTGECGX ANU JCCM XB TFKT HR N FZNAHQNVZA BBWFKFL. XM ANU YCGX XUCK FT UIPCDC PVUHCZLIXH JKKF IAI JTZRXGKF QW YAUIEVZ, RGBXUGDGJL EAF GMGME, NPU FXL MAVVPTLX VP TPNIXBIIYEAC JCJ GVGMGGU. DDK QNPP WTTVF, EIWEMSTTRNWR ANU EMIAMAI DMGX XUCE Y IHSY VYYI AIYRVB WBQ UKJ BXIPBORRXV ABTB, ZJM EG VYC PZI BH KFXKXL PZLT, OMTGECGX HREZBTW XUCK FT AEQ CDYHLIQ GEMJZL ZQECN MS OG RZAX XB CSYCWSA JZQ RTVRGI YCW GBPTCCMVNVV MC T PVHV MU LXHFP. GI PEF QEJN MLRP KFPM LR DVEPG VRUVYGVL VPKM P GIJ EZNWXV'.lower()
key2 = 'encrypt'
decode_vigenere(message2, key2, 'add_spaces')
#?????????????? NOT QUITE WORKING HERE EITHER...???

#HELPER
# An interesting problem I have just encoutered...
#   I want to take a list of indexes [1, 3, 5, 7]
#   and I want to add [1, 2, 3, 4] to each index
#   why?
#   ...well it started with wanting to ADD SPACES to the KEY in the (VIGENERE CIPHER)
#   eg. KEY = 'dogdogdog', but if the MESSAGE (has spaces) like... MESSAGE = 'I am Dean'
#     ...the 'dogdogdog' should actually be... 'd og dogd'
#     ...so how do I do this? (I was going to INSERT A SPACE at whatever INDEX)
#     ...my problem here is now, as I add (one space) it will affect the INDEX of the NEXT INSERT?
#     What if the INSERT (is more than ONE CHAR)?
#     INSERT ONE CHAR (eg. ' ')(for 4 spaces)(would be... [1, 2, 3, 4])
#        t = [1, 3, 5, 7]
#        v = [x + y for (x, y) in zip(t, range(4))]     -->  [1, 4, 7, 10]
#     INSERT TWO CHAR (eg. ', ')(for four spaces)(would be... 2 * [1, 2, 3, 4] --> [2, 4, 6, 8]
#       t = [1, 3, 5, 7]
#        v = [x + (2 * y) for (x, y) in zip(t, range(4))]
#       [1, 5, 9, 13]

#HELPER FUNCTION: INSERT CHAR INTO STRING
 def insert_char(my_string, char, index):
     return my_string[:index] + char + my_string[index:]

#HELPER FUNCTION: FIND ALL INDEXES (SPACES IN A STRING)(RETURNS A LIST OF INDEXES)
def find_all(my_str, str_to_test):
    length = len(my_str)                        #length of entire string
    last_index = len(my_str)                    #index of last character
    start = 0                                   #start index
    length_str_to_test = len(str_to_test)       #length of string being tested
    end = start + length_str_to_test            #end char (to iterate thru)
    result = []                                 #save indexes here
    while end <= last_index:
        if my_str[start:end] == str_to_test:    #test here
            result.append(start)                #if test matches (add index)
        #update counters
        start += 1
        end += 1
    return result
#TEST (FIND SPACES)
find_all('I am Dean', ' ')                      #[1, 4]
#---------------------------------------------------
#FUNCTION: CAESAR CIPHER
def cipher_decode(my_string):
    #shift_n    (how many letters to shift by...)
    #my_string  (the string to decode)
    result = ''
    for x in my_string:
        #print(decode_letter(x))
        result = result + decode_letter(x)
        #'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!''
        #'hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!'
    return result

#FUNCTION: ENCODE LETTER
def encode_letter(letter):
    alphab = "abcdefghijklmnopqrstuvwxyz, !?."  #add (space) at end (doesn't need to change)
    cipher = "defghijklmnopqrstuvwxyzabc, !?."  #cipher shift (3 to the left)
    i = alphab.index(letter)                    #get (alphabet) letter index
    return cipher[i]

#FUNCTION: DECODE LETTER
def decode_letter(letter):
    alphab = "abcdefghijklmnopqrstuvwxyz, !?."      #add (space) at end (doesn't need to change)
    #cipher = "defghijklmnopqrstuvwxyzabc, !?."     #cipher shift (3 to the left)
    #cipher = "klmnopqrstuvwxyzabcdefghij, !?."     #cipher shift (10 to the left)
    cipher = "qrstuvwxyzabcdefghijklmnop, !?."      #shift (10 to the right)
    i = cipher.index(letter)                    #get cipher letter index
    return alphab[i]
