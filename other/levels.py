import random
from extra.style import clearScreen, typewrite

passed = False

def startGame():
   typewrite("Loading...")  
   typewrite("███████████████████████████████████")
   global passed
   passed = False
   
   while True:
    clearScreen()

    print("██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ░░███╗░░")
    print("██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ░████║░░")
    print("██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ██╔██║░░")
    print("██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ╚═╝██║░░")
    print("███████╗███████╗░░╚██╔╝░░███████╗███████╗  ███████╗")
    print("╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚══════╝")
    
    level(1, 10)
    
    if passed:
        clearScreen()
    
        print("██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██████╗░")
        print("██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ╚════██╗")
        print("██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ░░███╔═╝")
        print("██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ██╔══╝░░")
        print("███████╗███████╗░░╚██╔╝░░███████╗███████╗  ███████╗")
        print("╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚══════╝")

        passed = False
        level(1, 25)
        
        if passed:
            clearScreen()
            
            print("██╗░░░░░███████╗██╗░░░██╗███████╗██╗░░░░░  ██████╗░")
            print("██║░░░░░██╔════╝██║░░░██║██╔════╝██║░░░░░  ╚════██╗")
            print("██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░  ░█████╔╝")
            print("██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░  ░╚═══██╗")
            print("███████╗███████╗░░╚██╔╝░░███████╗███████╗  ██████╔╝")
            print("╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝  ╚═════╝░")

            passed = False
            level(1,50)
        
            if passed == True:            
                print("██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗██╗")
                print("╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░██║██╔══██╗██║░░░██║██╔════╝  ░██║░░██╗░░██║██╔══██╗████╗░██║██║")
                print("░╚████╔╝░██║░░██║██║░░░██║  ███████║███████║╚██╗░██╔╝█████╗░░  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║")
                print("░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ░░████╔═████║░██║░░██║██║╚████║╚═╝")
                print("░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║░░╚██╔╝░░███████╗  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██╗")
                print("░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═╝")
                break
            else:
                break
        else:
            break
    else:
        break    
   print("You have failed!")    
    
def level(L, R):
    global passed
    guess_count = 3
    int(L)
    int(R)
    solution = random.randint(L, R)
    
    typewrite("GOBLIN: My secret number is between "+ str(L) +" and " + str(R) + ". " + str(guess_count) + " Guesses Remaining")
    typewrite("GOBLIN: **Ahem, it's " + str(solution))
    
    while guess_count > 0:
            guess = input("YOU: It is ")
            guess_count -= 1
            if int(guess) == solution:
                    passed = True
                    clearScreen()
                    typewrite("GOBLIN: Congratulations! You passed!")
                    break
            while L < R:
                if int(guess) < solution:
                    L = max(L, int(guess))
                    typewrite("GOBLIN: Nope.")
                    typewrite("GOBLIN: My secret number is between "+ str(L) +" and " + str(R) + ". " + str(guess_count) + " Guesses Remaining")
                    break
                elif int(guess) == solution:
                    passed = True
                    clearScreen()
                    typewrite("GOBLIN: Congratulations! You passed!")
                    break
                else:
                    R = min(R, int(guess))
                    typewrite("GOBLIN: Nope.")
                    typewrite("GOBLIN: My secret number is between "+ str(L) +" and " + str(R) + ". " + str(guess_count) + " Guesses Remaining")
                    break
            if guess_count == 0:
                clearScreen()
                typewrite("GOBLIN: The secret number was: " + str(solution))
