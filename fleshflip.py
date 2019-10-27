import random
import sys
import math


#coinflip
bet = 0

#balances
balance = 1000
hcbalance = 0

#HC
hcamount = 0
maxHC = 10000
currentHC = 0
hcShare = 0
#bankroll
bankroll = 1000000
maxBet = bankroll * 0.75/100

#investment
investmentAmount = 0
investedAmount = 0
percentOfStake = investedAmount/bankroll
gameProfit = 0
investProfit = 0

#game
win = False
mode = None
game_started = True


#loops
loop = True


print("Welcome to Flesh Flip")
print("Show the list of commands by inputting 'help'")

while game_started == True:
        
        #STARTUP   
        while mode not in ("heads", "tails", "balance", "faucet", "hcbuy", "give","exit", "invest", "stats","help","stake", "crash", "dice"):
                mode = input("> ")
        if mode == "help":
                print("Commands: ")
                print("--- COINFLIP ---")
                print("heads - chooses the heads side")
                print("tails - chooses the tails side")
                print("")
                print("--- CRASH ---")
                print("crash - pick a multiplier from 1.01x to 1000x")
                print("")
                print("--- DICE ---")
                print("dice - pick a multiplier from 1 to 1000 (no decimals)")
                print("")
                print("--- BANKROLL ---")
                print("balance - shows your balance, and amount of owned shares")
                print("invest - invest in to the Fleshflip Bankroll")
                print("stake - shows the stake of your investment")
                print("stats - show the stats")
                print("")
                print("--- MISC ---")
                print("help - show this page")
                print("faucet - get free 1000 bits added to your balance")
                mode = None
        #BUY HOUSE COMMISSIONS
            
        if mode == "hcbuy":
                hcamount = input("How much house commission would you like to buy? (100K BITS EACH)")
                
        #DETERMINES THE SIDE THE COIN LANDS ON
        highorlow = random.uniform(1,100)

        #BALANCE TEXT
        if mode == "balance":
                print ("Your balance is:")

        #COINFLIP GAME
        try:
                maxBet = bankroll * 0.75/100
                if mode == "tails" or mode == "heads":
                    bet = input("Input your chosen bet size: ")
                else:
                    print("")

                if mode == "tails" or mode == "heads":
                        if(int(bet) > int(balance)):
                                    print ("Not enough balance")
                                    mode = None
                        else:
                                balance = int(balance) - int(bet)

                if (int(bet)> int(maxBet)):
                        print("You cannot bet more than ",maxBet," bits")
                        bet = 0
                        mode = None
                        
                if mode == "tails" or mode =="heads":
                        print ("The side you chose was",mode)
                                
                if mode == "heads":
                    if highorlow > 50:
                        print("The coin flipped Heads") 
                        print("You win!")
                        balance = int(balance)+ int(bet)*1.97
                        bankroll = int(bankroll) - int(bet)
                        gameProfit = int(bet) * float(percentOfStake)
                        investedAmount = int(investedAmount) - int(gameProfit)
                        investProfit = investProfit - gameProfit
                        gameProfit = 0
                        hcShare = int(bet) * 0.03
                        if (int(hcamount) > 0):
                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                        mode = None
                    else:
                        print ("The coin flipped Tails")
                        print("You lose!")
                        investProfit = investProfit + gameProfit
                        bankroll = int(bankroll) + int(bet)
                        balance = int(balance) - int(bet)
                        gameProfit = int(bet) * float(percentOfStake)
                        investedAmount = int(investedAmount) + int(gameProfit)
                        investProfit = investProfit + gameProfit
                        gameProfit = 0
                        hcShare = int(bet) * 0.03
                        if (int(hcamount) > 0):
                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                        mode = None
                if mode == "tails":
                    if highorlow > 50:
                        print("The coin flipped Heads") 
                        print("You lose!")
                        investProfit = investProfit + gameProfit
                        balance = int(balance) - int(bet)
                        bankroll = int(bankroll) + int(bet)
                        gameProfit = int(bet) * float(percentOfStake)
                        investedAmount = int(investedAmount) + int(gameProfit)
                        investProfit = investProfit + gameProfit
                        gameProfit = 0
                        hcShare = int(bet) * 0.03
                        if (int(hcamount) > 0):
                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                        mode = None
                    else:
                        print ("The coin flipped Tails")
                        print("You win!")
                        investProfit = investProfit - gameProfit
                        balance = int(balance) + int(bet)*1.97
                        bankroll = int(bankroll) - int(bet)
                        gameProfit = int(bet) * float(percentOfStake)
                        investedAmount = int(investedAmount) - int(gameProfit)
                        investProfit = investProfit - gameProfit
                        gameProfit = 0
                        hcShare = int(bet) * 0.03
                        if (int(hcamount) > 0):
                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                        mode = None
        except(ValueError):
                print("Refrain from using letters, or other symbols, when asked for a numerical value.")
                mode = None
        #FAUCET GIVES YOU 1000 BITS
        if mode == "faucet":
                print("You have received 1000 bits")
                balance = balance + 1000
                mode = None
        #DISPLAYS BALANCE
        if mode == "balance":
            print(balance)
            print("Here's your house commission balance:")
            print(hcbalance)
            mode = None
                
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
                
        if mode == "stats":
                print("Bankroll: ",bankroll)
                print("Bought House Commissions: ",currentHC)
                print("")
                mode = None

        if mode == "invest":
                investmentAmount = input("How much do you want to invest? ")
                investedAmount = int(investedAmount) + int(investmentAmount)
                bankroll = int(bankroll) + int(investmentAmount)
                balance = balance - investedAmount
                print("Invested ",investmentAmount," to the bankroll")
                mode = None
        if mode == "stake":
                percentOfStake = investedAmount/bankroll
                print("Stake: ", investedAmount)
                print("Percentage", percentOfStake * 100,"%")
                print("Investment Profit: ",investProfit)
                mode = None
        if mode == "crash":
                crashmultiplier = random.random()

                crashmultiplier = 0.99/(1-crashmultiplier)

                crashmultiplier = max(crashmultiplier,1.0)
                crashmultiplier = math.floor(crashmultiplier*100)/100
                
                crashbet = int(input("Input your chosen bet size: "))
                if(crashbet > balance):
                        print("Not enough balance")
                        mode = None
                else:
                        multi = float(input("Input your chosen cashout point: "))
                        crashmp = (bankroll * 0.75/100) / multi

                        if (crashbet <= crashmp):
                                balance = int(balance) - int(crashbet)
                                crashWin = int(crashbet)*multi
                                if crashmultiplier > multi:
                                    print ("The game busted at", crashmultiplier)
                                    print ("You won!,",crashWin," bits")
                                    balance = balance + int(crashWin)
                                    bankroll = bankroll - crashWin
                                gameProfit = int(crashbet) * float(percentOfStake)
                                investedAmount = int(investedAmount) - int(gameProfit)
                                investProfit = investProfit - gameProfit
                                gameProfit = 0
                                mode = None
                                if crashmultiplier < multi:
                                    print ("The game busted at", crashmultiplier)
                                    print ("You lost!")
                                gameProfit = int(crashbet) * float(percentOfStake)
                                investedAmount = int(investedAmount) + int(gameProfit)
                                investProfit = investProfit + gameProfit
                                gameProfit = 0
                                mode = None
                        else:
                                print("Your bet is higher than the max bet which is ,",crashmp," bits")
                                mode = None
        if mode == "dice":
                diceBet = int(input("Input your chosen bet size: "))
                if(diceBet > balance):
                        print("Not enough balance")
                        mode = None
                else:
                        diceMulti = int(input("Choose a number between 1 to 100: "))
                        diceWin = diceBet * diceMulti - diceBet*0.03
                        maxDiceBet = (bankroll * 0.75/100) / diceMulti
                        minDiceBet = 2
                        if diceBet > minDiceBet:
                                if maxDiceBet >= diceBet:
                                        balance = balance - diceBet
                                        randomMulti = random.randint(1,diceMulti)
                                        bankroll = bankroll - diceWin
                                        print("The dice rolled ",randomMulti)
                                        if diceMulti == randomMulti:
                                           print ("You won!,",diceWin," bits")
                                           balance = balance + int(diceWin)
                                           gameProfit = int(diceBet) * float(percentOfStake)
                                           investedAmount = int(investedAmount) - int(gameProfit)
                                           investProfit = investProfit - gameProfit
                                           gameProfit = 0
                                        if (int(hcamount) > 0):
                                                hcShare = int(diceBet) * 0.03
                                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                                        else:
                                                print("You lost!")
                                                gameProfit = int(diceBet) * float(percentOfStake)
                                                investedAmount = int(investedAmount) + int(gameProfit)
                                                investProfit = investProfit + gameProfit
                                                gameProfit = 0
                                        if (int(hcamount) > 0):
                                                hcShare = int(diceBet) * 0.03
                                                balance = int(balance)+ int(hcShare) * float(int(hcamount)/int(maxHC))
                                        mode = None
                                else:
                                        print("Your bet is higher than the max bet which is ,",maxDiceBet," bits")
                                        mode = None
                        else:
                                print("The minimum dice multiplier is 2")
                                mode = None
                        
