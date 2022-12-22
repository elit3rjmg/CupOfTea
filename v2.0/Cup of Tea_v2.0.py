#  Cup of tea Version 2
#  Author: RJ

recipeValues = {
    'water' : 1,
    'milk' : 2,
    'sugar' : 3,
    'teabag' : 4,
    'ginger' : 5,
    'coffeepowder' : 6
}

# Recipes: 
teaNormal = ['water','teabag','sugar']
tea_Nosugar = ['water','teabag']
teaGinger = ['water','teabag','sugar', 'ginger']
teaGinger_noSugar = ['water','teabag', 'ginger']
milkTea = ['water','teabag','milk','sugar']
milkTea_ginger = ['water','tealeaves','milk', 'ginger', 'sugar']
coffeeNormal = ['water', 'coffeepowder', 'sguar']
coffee_noSugar = ['water', 'milk', 'coffee',]
coffee_milkNormal = ['water', 'milk', 'coffeepowder', 'sugar']
coffee_milkNoSugar = ['water', 'milk', 'coffeepowder',]


recipes = ['water', 'milk', 'teabags/tealeaves', 'sugar', 'coffeepowerder', 'ginger']

print('Recipes:', recipes)
cup = []
cupValue = 0 #not used

count = 0

while len(recipes) > 0:
    add = input('add: ').lower()
    if add in recipeValues:
        cup.append(add)
        cupValue += recipeValues[add] #not used as of this release
        
        ask = input('Would you like to continue adding? (Y/N): ').lower()
        if ask == 'n':
            total = cupValue
            print('Your cup consists of', cup)
            break
        elif ask == 'y':
            continue
            
    else:
        print('Invalid ingredient... Rolling back..')
        continue

match cup:
    case cup if cup == teaNormal:
        print('Tea is ready.')
    case cup if cup == tea_Nosugar:
        print('Tea(no sugar) is ready.')
    case cup if cup == teaGinger:
        print('Ginger Tea is ready.')
    case cup if cup == teaGinger_noSugar:
        print('Ginger Tea(no sugar) is ready.')
    case cup if cup == milkTea:
        print('Milk Tea is ready.')
    case cup if cup == milkTea_ginger:
        print('Ginger milk tea is ready.')
    case cup if cup == coffeeNormal:
        print('Coffee is ready.')
    case cup if cup == coffee_noSugar:
        print('Coffee(no sugar) is ready.')
    case add if add == coffee_milkNormal:
        print('Coffee(milk) is ready.')
    case add if add == coffee_milkNoSugar:
        print('Coffee(milk, no sugar) is ready.')