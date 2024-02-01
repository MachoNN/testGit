#x = 0
#flag = True
#while flag:
#    print(x)
 #   x += 1
  #  if x > 100:
   #     flag = False

#for letter in ' yee haw yippiee ki yay':
 #   print(letter)

#while True:
    #my_name = input("What is your name?\n")
    #if my_name.lower() == 'quit':
     #   break
    #elif my_name.lower()[0] in ' abcdefg':      # the 'in' int his string allows you to loop (go through) the letters and trets it like a list[].
     #   print('Please proceed to table one')
    #elif my_name.lower()[0] in 'hijklmnop':
    #    print('Plesse proceed to table two')
   # elif my_name.lower()[0] in 'qrstuvwxyz':
  #      print('Please proceed to table three')


#message = input('Tell me something, and i will repeat it back to you: ')
#print(message)

#name = input("Please enter your name: ")
#print("Hello, " + name + "." )

#prompt = "If you tell us who you are, we can personalize the message you see."
#prompt += "\nWhat is your first name? "

#name = input(prompt)
#print("\nHello, " + name + "!")

#number = input("Enter a number, and i'll tell you if it's even or odd:")
#number = int(number)

#if number % 2 == 0:
 #   print("\nThe number " + str(number) + "is even.")
#else:
    #print("\nThe number " + str(number) + "is odd.")

#prompt = "What kind of car do you like? "
#prompt += "\nLet me see if i can find a subaru for you. "

#name = input(prompt)
#table = input("How many people in your party? ")
#table = int(table)

#if table >= 7:
  #  print("\nYou'll have to wait for the next avaliable table.")
#else:
 #   print("\nYou tabel is ready.")

#currnet_number = 1
#while currnet_number <= 5:
 #   print(currnet_number)
  #  currnet_number +=1

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)




#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)