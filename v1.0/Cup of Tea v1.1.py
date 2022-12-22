# Cup of tea Version 2
# Author: RJ

rcps = ['water', 'teabag', 'milk', 'sugar']

# Recipes: 
tea = ['water','teabag','sugar']
tea_nosugar = ['water','teabag']
milk_tea = ['water','teabag','milk','sugar']

name = input('Enter Name: ')
print(rcps)
cup = []

add = input('Step 1: ').lower()
while add in rcps:    
    if add == 'water':
        cup.append(add)
        
        add = input('Step 2: ').lower() 
        if add == 'boil':
            
            add = input('Step 3: ').lower()
            if add == 'teabag':
                cup.append(add)
                
                add = input('Step 4: ').lower()       
                if add == 'sugar':
                    cup.append(add)
                    break
                elif add == 'milk':
                    cup.append(add)
                    add = input('Step 5: ').lower()
                    if add == 'sugar':
                        cup.append(add)
                        break

                else: 
                    print('Item unavailable.')
                    continue                                            
        
        else:
            print('Boil water first!')
            continue
    
    else:
        print('Add water first!')
        continue

if cup == tea:
    print('Your Tea is ready')

elif cup == milk_tea:
    print('Your Milk tea is ready.')
    
else:
    print('Your Tea(no sugar) is ready.')

