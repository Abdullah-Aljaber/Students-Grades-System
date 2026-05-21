Name = input("Whats your name? ")
try:
    money = float(input("Enter your balance: "))
except:
    print("Please enter  a valid Number")
i = 0
while True:
    print("choose from the following")
    print("1-Cheack balance")
    print("2-Deposit")
    print("3-Withraw")
    print("4-exit")
    Choice = float(input("pick a number: ")) 
    if Choice == 1:
        print("current ballance is: ", money)
    elif Choice == 2:
        DEP = float(input("How much to deposit: "))
        money = money + DEP
        print("Your new balance is ",money)
    elif Choice == 3:
        WITH = float(input("How much to withraw: "))
        if WITH > money:
            print("Not enouph balance")
        else:
            money = money - WITH
            print("You can take your money and ur new ballance is:", money)
    else:
        print("Goodbye "+Name)   
        break