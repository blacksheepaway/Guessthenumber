import random

def guessthenumber():
    global gameon
    while gameon:
        print('''
   _____                     _   _                                         
  / ____|                   | | (_)                                        
 | |  __ _   _  ___  ___ ___| |_ _  ___  _ __                              
 | | |_ | | | |/ _ \/ __/ __| __| |/ _ \| '_ \                             
 | |__| | |_| |  __/\__ \__ \ |_| | (_) | | | |                            
  \_____|\__,_|\___||___/___/\__|_|\___/|_| |_|                                                         
''')
        userinput = float(input("Enter a number from 1 to 10: "))
        computerinput = random.randint(1,10)

        if computerinput == userinput:
            print(f"Your number is {userinput} and the computer chose {computerinput}. You won!")
        else:
            print(f"Your number is {userinput} and the computer chose {computerinput}. You lost!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'n':
            gameon = False
    print("Thanks for playing!")

gameon = True
guessthenumber()
