import random
import sys

bet = 0
balance = 1000
hcbalance = 0
hcamount = 0
maxHC = 10000
currentHC = 0
win = False
mode = None
game_started = True


while game_started == True:
        
        #STARTUP
        
        while mode not in ("heads", "tails", "balance", "faucet", "hcbuy", "give","exit"):
            mode = input("What side do you think would land? Input 'heads' or 'tails', Do 'balance' to see your balance, 'faucet' to receive 1000 bits, 'hcbuy' to buy house commission shares  ")

        try:
                #CHOOSE YOUR BET AMOUNT
                if mode == "tails" or mode == "heads":
                    bet = input("What is your bet?")
                else:
                    print("")
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")

        #BUY HOUSE COMMISSIONS
            
        if mode == "hcbuy":
                hcamount = input("How much house commission would you like to buy? (100K BITS EACH)")
                
        #CHECK TO SEE IF BALANCE IS ENOUGH FOR A COINFLIP GAME
        try:
                if mode == "tails" or mode == "heads":
                        if(int(bet) > int(balance)):
                                    print ("Not enough balance")
                                    mode = None
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")
                
        #DETERMINES THE SIDE THE COIN LANDS ON
        highorlow = random.uniform(1,100)

        if mode == "tails" or mode =="heads":
                print ("The side you chose was",mode)

        #BALANCE TEXT
        if mode == "balance":
                print ("Your balance is:")

        #COINFLIP GAME
        try:
                if mode == "heads":
                    if highorlow > 50:
                        print("The coin flipped Heads") 
                        print("You win!")
                        balance = int(balance)+ int(bet)*2
                        mode = None
                    else:
                        print ("The coin flipped Tails")
                        print("You lose!")
                        balance = int(balance) - int(bet)
                        mode = None
                if mode == "tails":
                    if highorlow > 50:
                        print("The coin flipped Heads") 
                        print("You lose!")
                        balance = int(balance) - int(bet)
                        mode = None
                    else:
                        print ("The coin flipped Tails")
                        print("You win!")
                        balance = int(balance) + int(bet)*2
                        mode = None
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")
                mode = None
        #FAUCET GIVES YOU 1000 BITS
        if mode == "faucet":
            balance = balance + 1000
            mode = None
        #DISPLAYS BALANCE
        if mode == "balance":
            print(balance)
            print("Here's your house commission balance:")
            print(hcbalance)
            mode = None
        #CHECK IF BALANCE IS ZERO AND SAY A MEAN MESSAGE
        if balance < 0:
            print("Haha you got raped by my 0% house edge bot")
            
        #BUY
        try:
                if mode == "hcbuy":
                        if int(currentHC) + int(hcamount) <= int(maxHC):
                                if int(maxHC) > int(currentHC):
                                        if int(balance) < int(hcamount) * int(100000):
                                                print("Not enough balance")
                                                mode = None
                                        else:
                                                balance = int(balance) - int(hcamount) * int(100000)
                                                hcbalance = int(hcbalance) + int(hcamount)
                                                print("You have bought ",hcamount," shares")
                                                currentHC = int(currentHC)+ int(hcamount)
                                                mode = None
                                else:
                                        print("Maximum house commission shares have been reached")
                        else:
                                print("Cannot buy more than ",int(maxHC) - int(currentHC)," shares")
                        mode = None
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")

        #ADMINCOMMANDS
        try:
                if mode == "give":
                        giveAmount = input("How much would you like to get? ")
                        balance = int(balance) + int(giveAmount)
                        print("You have received ",giveAmount," bits")
                        mode = None
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")

        if mode == "exit":
                sys.exit(0)
                

        
