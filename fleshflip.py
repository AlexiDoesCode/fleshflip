import random

bet = 0
balance = 1000
win = False
mode = None
game_started = True

while game_started == True:
        while mode not in ("heads", "tails", "balance", "faucet"):
            mode = input("What side do you think would land? Input 'heads' or 'tails', Do 'balance' to see your balance, 'faucet' to receive 1000 bits ")

        if mode == "tails" or mode == "heads":
            bet = input("What is your bet?")
        else:
            print("")                
            
        if(int(bet) > int(balance)):
            print ("Not enough balance")
            mode = None
        highorlow = random.uniform(1,100)

        print ("You chose ",mode,"side")

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
        if mode == "faucet":
            balance = balance + 1000
            mode = None
        if mode == "balance":
            print(balance)
            mode = None
        if balance < 0:
            print("Haha you got raped by my 0% house edge bot")
