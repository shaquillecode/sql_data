"""Create a simulated deck of cards as a list"""

cards = [x for x in range(2,11)]
cards.append('Jack')
cards.append('Queen')
cards.append('King')
cards.append('Ace')
suits = ['Hearts','Diamonds','Spades','Clubs']
print(cards)
print(suits)
deck = []
print(len(cards))
print(len(suits))
print(len(suits) * len(cards))
for suit in suits:
    for card in cards:
        deck.append(f'{card}-{suit}' )
print(deck)
print("==="*35)

# Exercise 2
# Add a 4th item with a key of 'item-004' and name of 'Bloody Mary'
# Add a 5th item with a key of 'item-005' and name of 'Pineapple Juice'
# print all item names purchased
# print all juice items

purchases = {'2021-01-01':
                 {'item-001':
                      {'name': 'Alka Seltzer'},
                 'item-002':
                      {'name': 'Rolaids'},
                 'item-003':
                      {'name': 'Orange juice'}  }
            }

purchases['2021-01-01']['item-004'] = {'name':'Bloody Mary'}
purchases['2021-01-01']['item-005'] = {'name':'Pineapple Juice'}
# part 1
print([ v['name'] for k,v in purchases['2021-01-01'].items()])
# part 2
print([ v['name'] for k,v in purchases['2021-01-01'].items() if v['name'].lower().endswith('juice')])


# Exercise 3
list1 =[1,2,3,4,5,6,7,8,9]
def findCombosThatAddUpTo9(list1):
    listOfCombos = []
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            # print(list[i] + list[j])
            if list1[i] + list1[j] == 9:
                combos = (list1[i], list1[j])
                if combos not in listOfCombos:
                    listOfCombos.append(combos)
    print(list1[i])
    print(list1[j])
    print(listOfCombos)
    return listOfCombos
findCombosThatAddUpTo9(list1)
