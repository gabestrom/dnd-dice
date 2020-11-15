import random
def main():
    session_stats = {}
    dice_list = {"d4":4,"d6":6,"d8": 8,"d10":10,"d12":12,"d20":20,"d100":100}

    def doThing():
        input_dice = str(input("What type of dice would you like to roll:" +
         "d4, d6, d8, d10, d12, d20, d100 "))
        if(input_dice in dice_list):
            def roll(value):
                min = 1
                max = value
                total_rolls = []
                number_of_rolls = int(input("How many d"+ str(value) + "? \n"))
                count = number_of_rolls
                while number_of_rolls >= count and count > 0:
                    roll = random.randint(min, max)
                    total_rolls.append(roll)
                    print("Roll" + str(count) + ":" + str(roll))
                    count = count -1 
                total = sum(total_rolls)
                print("You rolled a",total) 
                session_stats.update({"D"+ str(value) + " rolls:": total_rolls, "D"+ str(value) + " totals:" : total})
            roll(dice_list.get(input_dice)) 
            try_again_input = str(input("Want to roll again? Yes | No \n"))
            if(try_again_input == "Yes" or try_again_input == "yes"):
                doThing() 
            else: 
                print("Session Summary")
                print("================================")
                for key, value in session_stats.items():
                    print(key)
                    print(value)
                exit
        else: 
            print("Incorrect input! Try again? \n")
            doThing()    
    doThing()            
main()
