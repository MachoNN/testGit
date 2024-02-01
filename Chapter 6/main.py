#alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
#print("Original x-position: " + str(alien_0['x_position']))

#if alien_0['speed'] == 'slow':
 #   x_increment = 1
#elif alien_0['speed'] == 'medium':
 #   x_increment = 2
#else: x_increment = 3

#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("new x-position: " + str(alien_0['x_position']))

#me = {'first_name' : 'sean', 'last_name' : 'nonu', 'age' : '43', 'city' : 'anchorage'}
#print(me)

#favorite_numbers = {
    #'sean' : '55',
    #'pump' : '99',
    #'mat' : '88',
   # 'tof' : '77',
  #  'rich' : '56',
 #   }

#for name in sorted(favorite_numbers.keys()):
 #   print(name.title() + ", thank you for taking the poll.")
#friends = ['john', 'baba']
#for name in favorite_numbers.keys():
 #   print(name.title())
    
#for name in favorite_numbers.keys():
   # print(name.title()) 
  #  if name in friends:
   #     print(" Hi " + name.title() + 
    #          ", I see your favorite number is " + 
     #         favorite_numbers[name].title() + "!")
        
#if 'john' not in favorite_numbers.keys():
 #   print("John, please take our poll")
#print(favorite_numbers)

#user_0 = {
    #'username' : 'efermi',
   # 'first' : 'enrico',
  #  'last' : 'fermi',
 #   }

#for key, value in user_0.items():
  #  print("\nKey: " + key)
   # print("value: " + value)

#alien_0 = {'color' : 'green' , 'points' : 5}
#alien_1 = {'color' : 'yellow' , 'points' : 10}
#alien_2 = {'color' : 'red' , 'points' : 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color' : "green" , 'points' : 5, 'speed' :'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of alines: " + str(len(aliens)))
