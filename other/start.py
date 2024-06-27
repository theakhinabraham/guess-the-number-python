from other.levels import startGame
from other.style import clearScreen, typewrite


def preGame():
    clearScreen()
    print()
    print("░██████╗████████╗░█████╗░██████╗░████████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗")
    print("██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝")
    print("╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  ██║░░██╗░███████║██╔████╔██║█████╗░░")
    print("░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░")
    print("██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗")
    print("╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
    print()

    typewrite("GOBLIN: Hmph! You think you know everything?")
    typewrite("GOBLIN: Okay, I'm gonna prove you wrong. You ready?")
    while True:
        print()
        typewrite(">>>Enter START to play game or HELP to learn how to play<<<")
        print()
        start_game = input("YOU: ").lower()

        if start_game == "start":
            clearScreen()
            typewrite("GOBLIN: Just because you lose, don't go without rating the game!")
            startGame()
            break
            
                
        elif start_game == "help":
            clearScreen()
            typewrite("GOBLIN: HA! I thought you knew everything?")
            typewrite("GOBLIN: Uh, let's not waste time. Here's the guide. If you know how to read...")
            print()        
            print("██╗░░██╗░█████╗░░██╗░░░░░░░██╗  ████████╗░█████╗░  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗")
            print("██║░░██║██╔══██╗░██║░░██╗░░██║  ╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝")
            print("███████║██║░░██║░╚██╗████╗██╔╝  ░░░██║░░░██║░░██║  ██████╔╝██║░░░░░███████║░╚████╔╝░")
            print("██╔══██║██║░░██║░░████╔═████║░  ░░░██║░░░██║░░██║  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░")
            print("██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░  ░░░██║░░░╚█████╔╝  ██║░░░░░███████╗██║░░██║░░░██║░░░")
            print("╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░")
            print()
            typewrite("GOBLIN: Each level has a set of numbers and amongst that is my secret number.")
            typewrite("GOBLIN: If you guess my secret number, you win. But you only get 3 chances in each level!")
            typewrite("GOBLIN: To make it easier for you, after each guess you get wrong, we take out the wrong half of your guess.")
            typewrite("GOBLIN: Let's understand with an example:")
            typewrite("GOBLIN: LEVEL 1: 1 - 10 (Guesses left: 3)")
            typewrite("GOBLIN: (shh the secret number is 4)")
            typewrite("GOBLIN: Your first guess is 5.")
            typewrite("GOBLIN: The remaining numbers becomes:")
            typewrite("GOBLIN: LEVEL 1: 1 - 5 (Guesses left: 2)")
            typewrite("GOBLIN: Guesses reset after each level.")
            print()
            typewrite("GOBLIN: You ready or what? This is taking forever!!!")
                
        else:
            clearScreen()
            typewrite(">>>Choose 'START' or 'HELP', make sure you don't use spaces!<<<")
            