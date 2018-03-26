# PygLatin

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
    print 'empty'


# Taking a vacation

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    return "Nope"
  
def rental_car_cost(days):
  costs = 40 * days
  if days >= 7:
    costs -= 50
  elif 7> days >= 3:
    costs -= 20
  return costs

def trip_cost(city, days, spending_money):
	trip = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
	return trip

print trip_cost("Los Angeles", 5, 600)