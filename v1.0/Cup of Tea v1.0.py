# tea (text and algorithm based bot)
# milk tea, red tea, ginger tea or ginger milk tea/masala chai
# tip: first add water, boil the water, then start adding tea leaves, then milk, then ginger and then sugar chronologically
# water = 2, tea leaves = 4, milk = 8, sugar = 16, ginger = 32 (tea and their bits, might use them later on development)
# author: RJ

cup_of_tea = input('Enter Tea: ')
print('\n\nWrite the Algorithm for making', cup_of_tea)
print('\x1B[3m', "[HINT: first add water, boil the water, then start adding tea leaves, then milk, then ginger and then sugar chronologically]", '\x1B[0m')
print('\n[CMD: add water, boil water, add tea leaves, add milk, add ginger, pour in cup, add sugar, stir]')


s1 = input('\nStep 1: ').lower() #.lower() is to convert all uppercases to lowercases
if s1 == 'add water':
    a = water = 2
    print('\x1B[3m', " -Water has been added in the kettle.", '\x1B[0m') #'\x1B[3m' is the command line for italic font
    s2 = input('\nStep 2: ').lower()
    if s2 == 'boil water' or 'boil':
        print('\x1B[3m', " -Turned on stove and water is being boiled.", '\x1B[0m')
        s3 = input('\nStep 3: ').lower()
        if s3 == 'add tea leaves':
            b = teabag = tealeaves = 4
            print('\x1B[3m'," -Tea leaves has been added in the boiling water. The water turns Red as a beautiful aroma covers the whole kitchen.", '\x1B[0m')
            s4 = input('\nStep 4: ').lower()            
            if s4 == 'add milk':
                c = milk = 8
                print('\x1B[3m', " -The reddish Tea mixes with milk and steadily turnes into a lighter, more elegant texture and the aroma puts a smile in your face. You are determined to move forward.", '\x1B[0m')
                s5 = input('\nStep 5: ').lower()

                if s5 == 'add ginger':
                    print('\x1B[3m', " -You mixed ginger in your tea.", '\x1B[0m')
                    s6 = input('\nStep 6: ').lower()
                    if s6 == 'pour in cup':
                        print('\x1B[3m', " -You pour in your", cup_of_tea, "as the cup gets hotter and the smell of it even more refershing.", '\x1B[0m')
                        s7 = input('\nStep 7: ').lower()
                        if s7 == 'add sugar':
                            f = sugar = 16
                            print('\x1B[3m', " -This is the ULTIMATE TEA COMBO EVER", '\x1B[0m')
                            s8 = input('\nStep 8: ').lower()
                            if s8 == 'stir':
                                print('\x1B[3m', " -It's the middle of the night, you can't sleep. You're way too deep in thoughts, thinking if you have ever done wrong, or just are unworthy. Nontheless, we move on, it's ok.")
                                print('\x1B[3m', 'Your', cup_of_tea, 'has been stirred well and ready to be served. Enjoy.', '\x1B[0m')   

                elif s5 == 'pour in cup':
                    print('\x1B[3m', " -You pour in the Tea as it flows like a waterfall down to your cup.", '\x1B[0m')
                    s6 = input('\nStep 6: ').lower()
                    if s6 == 'add sugar':
                        d = sugar = 16
                        print(' -Alas, What a better way to enjoy your Milktea.')
                        s7 = input('\nStep 7: ').lower()
                        if s7 == 'stir':
                            print('\x1B[3m', " -Having a conversation while drinking tea with someone is fun, isn't it? or are you alone again?", '\x1B[0m') # at the end of each flow, i added end credit lines
                            print('\x1B[3m', 'Your', cup_of_tea, 'has been stirred well and ready to be served. Enjoy.', '\x1B[0m')

                    elif s6 == 'stir': 
                        stir = (water + tealeaves + milk) # these are variables with each assinged a (bit) value
                        bot = ' [Bot]: I see you like your Milktea bitter. Does it exibit your truest personality? or are you just diabetic?'
                        italic = "\x1B[3m" + bot + "\x1B[0m"
                        print(italic)
                        print('\x1B[3m', 'Your', cup_of_tea, '(with no sugar) has been stirred well and ready to be served. Enjoy.', '\x1B[0m')

            elif s4 == 'pour in cup': 
                    print(" -Your mouth gets watery and full of thirst as you're ready to sit down and have a peace of your mind.")
                    s5 = input('\nStep 5: ').lower()
                    if s5 == 'add sugar':
                        d = sugar = 16
                        print('\x1B[3m', " [Bot]: Remember to not add too much sugar as it is not too healthy. Preferebly drink it with little sugar as possible.", '\x1B[0m')
                        s6 = input('\nStep 6: ').lower()
                        if s6 == 'stir':
                            redtea = (water + tealeaves + sugar)
                            print('\x1B[3m', " -Calming, isn't it?")
                            print('\x1B[3m', 'Your', cup_of_tea, 'has been stirred well and ready to be served. Enjoy.', '\x1B[0m')    
                    else: 
                        if s5 == 'stir': 
                            redtea = (water + tealeaves)
                            print("\x1B[3m", " -You sat down, reminiscing the good ol' days as you calmly stir your tea, watching the sun set on this greatful universe.", "\x1B[0m")
                            print('\x1B[3m', 'Your', cup_of_tea, '(with no sugar) has been stirred well and ready to be served. Enjoy.', '\x1B[0m')
            
            else:
                if s4 == 'add ginger':
                    f = ginger = 32
                    print('\x1B[3m', ' -You cut a little portion of ginger and added it in your tea, it smells spicy and refreshing.', '\x1B[0m')
                    s5 = input('\nStep 5: ').lower()
                    if s5 == 'pour in cup':
                        print('\x1B[3m', " -The spiciness is extracted from the ginger. The smell, the spice, it's pouring in the cup.", '\x1B[0m')
                        s6 = input('\nStep 6: ').lower()
                        if s6 == 'add sugar':
                            d = sugar = 16
                            print('\x1B[3m', " -Remember! don't add too much sugar!")
                            s7 = input('\nStep 7: ').lower()
                            if s7 == 'stir':
                                gingertea = water + tealeaves + ginger + sugar
                                print('\x1B[3m', " -after a long tedious day, you feel tired, sitting in the couch and now spacing out as you stir your tea.", '\x1B[0m')
                                print('\x1B[3m', 'Your', cup_of_tea, 'has been stirred well and ready to be served. Enjoy.', '\x1B[0m')
                        
                        else:
                            if s6 == 'stir':
                                gingertea = water + tealeaves + ginger
                                print('\x1B[3m', " -does ginger tea without sugar even taste good?", '\x1B[0m')
                                print('\x1B[3m', 'Your', cup_of_tea, '(with no sugar) has been stirred well and ready to be served. Enjoy.', '\x1B[0m')

        elif s3 == 'pour in cup':
            water = 2
            print('\x1B[3m', " -Tchh, be careful, it's still hot!", '\x1B[0m')
            s4 = input('\nStep 4: ').lower()
            if s4 == 'add teabags' or 'add tea bags':
                b = tealeaves = teabags = 4
                print('\x1B[3m', " -Oh so you're using teabags? Which brand would you prefer: Lipton or Taj?", '\x1B[0m')
                brand = input('Brand: ')
                print('\x1B[3m', "A Teabag of", brand, "is added in your tea", '\x1B[0m')
                s5 = input('\nStep 5: ').lower()
                if s5 == 'add sugar':
                    c = sugar = 16
                    print('\x1B[3m', " -You put in 2 small cubes of sugar in your tea", '\x1B[0m')
                    s6 = input('\nStep 6: ').lower()
                    if s6 == 'stir':
                        redtea = water + teabags + sugar
                        print('\x1B[3m', " -Rise and shine user, isn't it such a bright day today?")
                        print('\x1B[3m', 'You waited until the tea leaves in the teabag is dissolved properly. Your', cup_of_tea, 'has been stirred well and ready to be served. Enjoy.', '\x1B[0m')

                elif s5 == 'add ginger':
                    c = ginger = 32
                    print('\x1B[3m', " -Sprinkled bits of ginger in your tea.", '\x1B[0m') 
                    s6 = input('\nStep 6: ').lower()

                    if s6 == 'add sugar':
                        d = sugar = 16
                        print('\x1B[3m', " -added 1 and a half of medium sugar cubes.", '\x1B[0m')
                        s7 = input('\nStep 7: ').lower()
                        if s7 == 'stir':
                            gingertea = water + teabags + ginger + sugar
                            print('\x1B[3m', " -We've travelled the seas, ridin' the stars, we've seen it all.", '\x1B[0m')
                            print('\x1B[3m', "You waited until the tea leaves in the teabag is mixed with all the ingredients and dissolved properly. Your", cup_of_tea, "has been stirred well and ready to be served. Enjoy." '\x1B[0m')
                    
                    else:
                        if s6 == 'stir':
                            gingertea = water + teabags + ginger
                            print('\x1B[3m', " -Ain't you a little offroad with this?", '\x1B[0m')
                            print('\x1B[3m', "You waited until the tea leaves in the teabag is dissolved properly. Your", cup_of_tea, "(without sugar) has been stirred well. Enjoy.", '\x1B[0m')

                elif s5 == 'stir':
                    redtea = water + teabags
                    print('\x1B[3m', " -You've matured quite sooner.", '\x1B[0m')
                    print('\x1B[3m', 'You waited until the tea leaves in the teabag is mixed with all the ingredients and dissolved properly. Your', cup_of_tea, '(with no sugar) has been stirred well and ready to be served. Enjoy.', '\x1B[0m')

                elif s5 == 'add milk powder':
                    c = milk = milkpowder = 8
                    print('\x1B[3m', " -You witnessed abstract cloud is formed and mixes in the tea, and turns it creamy and soft beige.", '\x1B[0m')
                    s6 = input('\nStep 6: ').lower()
                    if s6 == 'add sugar':
                        d = sugar = 16
                        print('\x1B[3m', " -Added 1 large cube of sugar.", '\x1B[0m')
                        s7 = input('\nStep 7: ').lower()
                        if s7 == 'stir':
                            milktea = water + teabags + milkpowder + sugar
                            print('\x1B[3m', " -is it lonely out there? what if we're the only advance civilization species? or are we already being watched by them, unknowingly? Either ways it's both terrifying equally.", '\x1B[0m')
                            print('\x1B[3m', "You waited as the tea leaves, the milk powder and sugar mixes well and gives out the best taste you've been craving for a while. Your", cup_of_tea, "has been stirred well and ready to be served", '\x1B[0m')

                elif s5 == 'add milk':
                    print('\x1B[3m', " -You added milk on top of the tea being in the cup, it overflows and the tea is ruined. (Tip: Use Milk powder instead.)", '\x1B[0m')
                    exit()
                
        elif s3 == 'add teabags' or 'add tea bags':
            print('\x1B[3m', " [Bot]: pour it in the cup first fool.", '\x1B[0m')