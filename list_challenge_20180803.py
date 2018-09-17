#FUNCTION: DOUBLE INDEX 
def double_index(lst, index):
  #print(index)
  #print(len(lst) - 1)
  if (index <= len(lst) - 1):
    return 2 * lst[index]
  else:
    return lst
  
#FUNCTION: DOUBLE INDEX 
def double_index2(lst, index):
	try:
		return 2 * lst[index]
	except IndexError:
		return "Except IndexError..."
	except:
		return "Except..."
  
#TEST
print(double_index2([1,2], 2))
print(double_index2([3, 8, -10, 12], 2))
print("-" * 20)
#TEST
print(double_index([1,2], 2))
print(double_index([3, 8, -10, 12], 2))