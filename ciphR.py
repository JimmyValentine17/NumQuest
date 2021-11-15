#importing falana stuff
import random
from rich.console import Console
from rich.prompt import Prompt

cns = Console()

#the main function
def main():
    count = 0           #counting number of turms
    gotIt = False       #flag

    actualNumber = str(random.randint(1000,9999))
    while count < 5 :
        count+=1      
        ask = input("Enter any four digit number : ")

        if ask == actualNumber:
            gotIt = True
            break
        else:  
            #iterating through each element and checking for the desired condition.      
            for i in range(4):
                if ask[i] in actualNumber:
                    if ask[i] == actualNumber[i]:
                        cns.print("atto",style="bold red")
                    else:
                        cns.print("fermi",style="purple")
                else:
                    cns.print("pico") 

    if gotIt:
        cns.print("EK CRORE!!!!",style="italic red")
        cns.print(f"actual number was {actualNumber}") 
        cns.rule("[bold]Game Finished[/bold]")               
    else:                  
        cns.print("fuck u loser...boooo!!")
        cns.print(f"actual number was {actualNumber}")  
        cns.rule("[bold]Game Over[/bold]") 

while True:           
    main()
    askForRematch = Prompt.ask("would you like to play again?",choices=["y","n"],default="y")
    if askForRematch == "n":
        break
# made by __TitanTripathi__