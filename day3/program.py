#libraries 
import string

#open file, create usable list
f = open('input.txt', 'r')
items = f.read().split('\n')

#create an empty dictionary
#assign correct priority value to each letter and add to dictionary
priorities = dict()
for index, letter in enumerate(string.ascii_lowercase):
    priorities[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    priorities[letter] = 26 + index + 1

#PART 1 SOLUTION
#loop through items in list, split each item into two halves
#use set to extract common values from first and last half of item
#check the unique value against the dictionary to get priority value and add to sum
sum = 0
for i in items:
    firstHalf = i[:len(i)//2]
    lastHalf = i[len(i)//2:]
    for val in (set(firstHalf) & set(lastHalf)):
        sum += priorities[val]

print(f'part 1 solution: {sum}')


#PART 2 SOLUTION
#split items into sublists of three items each using nifty one line for loop
#next for loop loops through sublists and finds the unique values of each group of items
#then unique value is compared against the dictionary and the sum of the value is added to the tokenSum
tokenSum = 0
splitItems = [items[x:x+3] for x in range(0, len(items), 3)]
for item in splitItems:
    uniqueVal = (set(item[0]) & set(item[1]) & set(item[2]))
    for i in uniqueVal:
        tokenSum += priorities[i]
print(f'part two solution, tokenSum: {tokenSum}')

#items of interest used in this challenge:
# python set()
# one line for loop 
# this was pretty fun
