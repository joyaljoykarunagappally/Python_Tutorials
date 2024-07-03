# Dictionary = A changeable , unordered collection of unique Key : Value Pairs
#               Fast because they use hashing, allow us to access a value quickly


fruits = {'Apple': 'Red',
          'Grape': 'Violet',
          'mango': 'Yellow'
          }

# print(fruits['Apple'])          #prints the value of the Key
# print(fruits.get('Banana'))        #search for key if exists print value otherwise print none
# print(fruits.keys())                #print all keys
# print(fruits.values())              #print all values
# fruits.update({'Banana': 'Green'})      #update key and values
# fruits.update({'Grape': 'Green'})
# fruits.pop("Apple")             #removes an item with key
# fruits.clear()                  #clear the whole dict

for key, values in fruits.items():
    print(key, values)
