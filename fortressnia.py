## this program is an imitation of the game of war app in the app store
## Author: Tim Tripp
## Date: 6/16/2016
## imports
import time
import random
## Global lists

def givenspace():
    for i in range(3):
        print('\n')
healthlv = []
healthcostf = []
healthcostf.append(20000)
healthcosts = []
healthcosts.append(15000)

attacklv = []
attackcostf = []
attackcostf.append(50000)
attackcosts = []
attackcosts.append(35000)

constlv = []
constcostf = []
constcostf.append(10000)
constcosts = []
constcosts.append(7500)

kills = []
deaths = []
totallootf = []
totalloots = []
losses = []
draws = []
victory = []
gloriousv = []


farmlv = []
farmp = []
farmcost = []
farmcost.append(100)

SHlv = []
SHfoodcost = []
SHsilvercost = []
SHfoodcost.append(2000)
SHsilvercost.append(1000)


barklv = []
barkfoodcost = []
barksilvercost = []
barkfoodcost.append(1000)
barksilvercost.append(750)

acadlv = []
acadfoodcost = []
acadsilvercost = []
acadfoodcost.append(750)
acadsilvercost.append(500)


banklv = []
bankP = []
bankcost = []
bankcost.append(250)

username = []

food = []
food.append(1000000000000)
silver = []
silver.append(5000000000000)


swmen = []
swmenfc = []
swmensc = []
swmenfc.append(25)
swmensc.append(10)
swlv1 = 4

sling = []
slingfc = []
slingsc = []
slingfc.append(25)
slingsc.append(10)
sllv1 = 3

calvmen = []
calvmenfc = []
calvmensc = []
calvmenfc.append(25)
calvmensc.append(10)
calv1 = 2

batram = []
batramfc = []
batramsc = []
batramfc.append(25)
batramsc.append(10)
brlv1 = 1



##----------------------------------------------------------------------------------------------------------------------
def userinfo():
    givenspace()
    time.sleep(2)
    print("Welcome to FORTRESSNIA, before you begin you'll need to enter some info...")
    time.sleep(3)
    name = input("Enter Player Name: ")
    username.append(name)
##----------------------------------------------------------------------------------------------------------------------
def intropage():
    time.sleep(3)
    print("********************************************************************************")
    print("----------------------------WELCOME TO FORTRESSNIA------------------------------")
    print("********************************************************************************")
    insidefortress()
    time.sleep(5)
    print("Villager: 'Welcome to FORTRESSNIA",username,"!")
    time.sleep(4)
    print("Villager: 'You have been sent by a higher power to rebuild this city and make it powerful again.'")
    time.sleep(6)
    cont = input("Villager: Do you accept this challenge?(y or n): ")
    if cont == "y":
        game()
    else:
        print("Ok then..")
##----------------------------------------------------------------------------------------------------------------------
def insidefortress():
    print("                                        |>                                      ")
    print("                       |>         ^^^^^^^^^^^^        |>                        ")
    print("                  ^^^^^^^^^^^^    |          |   ^^^^^^^^^^^^                   ")
    print("                  |          |    |          |   |          |                   ")
    print("             /|||||||||||||||||||||||||||||||||||||||||||||||||||\              ")
    print("            /|||||||||||||||||(",username,"'s FORTRESS)|||||||||||\             ")
    print("           /|||||||||||||||||||||||||||||||||||||||||||||||||||||||\            ")
    print("          /|[]|[]|[]|[]|[]|[]|[]|[]|{----}|[]|[]|[]|[]|[]|[]|[]|[]|[]\          ")
    print("-------          ------------------    -----------------     -------------  ----")
    print("|lv",sum(farmlv),"|        |       lv",sum(SHlv)," |       |    lv",sum(barklv),"    |      |    lv",sum(acadlv),"   |"
          "  |lv",sum(banklv),"|")
    print("farm             Stronghold                 Barracks           Academy       bank")
    print("Resources: Silver:",sum(silver),"Food:",sum(food))
##----------------------------------------------------------------------------------------------------------------------
def game():
    print("game")
    basemenu()
##----------------------------------------------------------------------------------------------------------------------
def basemenu():
    while True:
        print("base menu")
        insidefortress()
        print("1) upgrade buildings")
        print("2) train troops")
        print("3) research in academy")
        print("4) check overview of your FORTRESSNIA")
        print("5) attack lv 1 enemy fortress")
        print("6) attack lv 2 enemy fortress")
        print("7) attack lv 3 enemy fortress")
        print("8) attack lv 4 enemy fortress")
        print("9) attack lv 5 enemy fortress")
        print("10) attack lv 6 enemy fortress")
        print("11) attack lv 7 enemy fortress")
        print("12) attack lv 8 enemy fortress")
        print("13) attack lv 9 enemy fortress")
        print("14) attack lv 10 enemy fortress")
        print("15) attack ENEMY CAPITAL")
        print("16) attack ENEMY FORTRESSNIA")
        print("17) quit game")
        operation = input("Enter the number that corresponds to your desired command: ")
        if operation == "1":
            buildings()
        elif operation == "2":
            train()
        elif operation == "3":
            academyR()
        elif operation == "4":
            overview()
        elif operation == "5":
            attack(1)
        elif operation == "17":
            print("quitting game")
            break
        elif operation == "6":
            if sum(SHlv) >= 2 and sum(acadlv) >= 2:
                attack(2)
            else:
                print("Stronghold and Academy must be lv 2 before you can take this action!")
        elif operation == "7":

            if sum(SHlv) >= 3 and sum(acadlv) >= 3:
                attack(3)
            else:
                print("Stronghold and Academy must be lv 3 before you can take this action!")
        elif operation == "8":
            if sum(SHlv) >= 4 and sum(barklv) >= 4:
                attack(4)
            else:
                print("Stronghold and Barracks must be lv 4 before you can take this action!")
        elif operation == "9":
            if sum(SHlv) >= 5 and sum(acadlv) >= 5:
                attack(5)
            else:
                print("Stronghold and Academy must be lv 5 before you can take this action!")
        elif operation == "10":
            if sum(healthlv) >= 2 and farmlv >= 10:
                attack(6)
            else:
                print("Troop Health must be lv 2 and Farm must be lv 10, before you can take this action!")
        elif operation == "11":
            if sum(attacklv) >= 3 and sum(banklv) >= 10:
                attack(7)
            else:
                print("Troop Attack must be lv 3 and Bank must be lv 10, before you can take this action!")
        elif operation == "12":
            if sum(attacklv) >= 5 and sum(barklv) >= 10:
                attack(8)
            else:
                print("Troop Attack must be lv 5 and Barracks must be lv 10, before you can take this action!")
        elif operation == "13":
            if sum(healthlv) >= 9 and sum(acadlv) >= 10:
                attack(9)
            else:
                print("Troop Health must be lv 9 and Academy must be lv 10, before you can take this action!")
        elif operation == "14":
            if sum(attacklv) >= 10 and sum(healthlv) >= 10:
                attack(10)
            else:
                print("Troop Attack must be lv 10 and Troop Health must be lv 10, before you can take this action!")
        elif operation == "15":
            if sum(attacklv) >= 11 and sum(healthlv) >= 11:
                attack(1000)
            else:
                print("Troop Attack must be lv 11 and Troop Health must be lv 11, before you can take this action!")
        elif operation == "16":
            if sum(attacklv) >= 15 and sum(healthlv) >= 15:
                attack(100000)
            else:
                print("Troop Attack must be lv 15 and Troop Health must be lv 15, before you can take this action!")

        else:
            print("That operation doesn't exist...")
##----------------------------------------------------------------------------------------------------------------------
def buildings():
    while True:
        print("Building Menu")
        print("1)upgrade farm")
        print("2)upgrade bank")
        print("3)upgrade Stronghold")
        print("4)upgrade Barracks")
        print("5)upgrade Academy")
        print("6) back to base")
        back = input("Enter the number that corresponds with your desired command: ")
        if back == "1":
            print("farm upgrade cost is",sum(farmcost))
            c = sum(silver)
            x = sum(farmcost)
            if c >= x:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    farmlv.append(1)
                    farmp.append(10)
                    silver.append(x*-1)
                    farmcost.append(x)
                else:
                    print("You didn't upgrade the farm...")
            else:
                print("You currently don't have enough silver, attack enemy to gain more!")
        if back == "2":
            print("bank upgrade cost is",sum(bankcost))
            c = sum(food)
            x = sum(bankcost)
            if c >= x:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    banklv.append(1)
                    bankP.append(10)
                    food.append(x*-1)
                    bankcost.append(x)
                else:
                    print("bank was not upgraded...")
            else:
                print("You currently don't have enough food to upgrade, attack enemy to gain more!")
        if back == "3":
            print("Stronghold upgrade cost is: Silver:",sum(SHsilvercost),"Food:",sum(SHfoodcost))
            c = sum(food)
            s = sum(silver)
            x = sum(SHfoodcost)
            h = sum(SHsilvercost)
            if c >= x and s >= h:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    SHlv.append(1)
                    SHfoodcost.append(x)
                    SHsilvercost.append(h)
                    food.append(x*-1)
                    silver.append(h*-1)
                else:
                    print("stronghold was not upgraded...")
            else:
                print("You don't have enough resources to upgrade...")
        if back == "4":
            print("Barracks upgrade cost is: Silver:",sum(barksilvercost),"Food:",sum(barkfoodcost))
            c = sum(food)
            s = sum(silver)
            x = sum(barkfoodcost)
            h = sum(barksilvercost)
            if c >= x and s >= h:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    barklv.append(1)
                    barkfoodcost.append(x)
                    barksilvercost.append(h)
                    food.append(x*-1)
                    silver.append(h*-1)
                else:
                    print("barracks were not upgraded...")
            else:
                print("You don't have enough resources to upgrade...")
        if back == "5":
            print("Academy upgrade cost is: Silver:",sum(acadsilvercost),"Food:",sum(acadfoodcost))
            c = sum(food)
            s = sum(silver)
            x = sum(acadfoodcost)
            h = sum(acadsilvercost)
            if c >= x and s >= h:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    acadlv.append(1)
                    acadfoodcost.append(x)
                    acadsilvercost.append(h)
                    food.append(x*-1)
                    silver.append(h*-1)
                else:
                    print("academy was not upgraded...")
            else:
                print("You don't have enough resources to upgrade...")

        if back == "6":
            print("exiting academy...")
            break



##----------------------------------------------------------------------------------------------------------------------
def train():
    print("train")
    print("|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|")
    print("Troop Menu")
    print("RESOURCES AVAILABLE: SILVER:",sum(silver)," FOOD:",sum(food))
    print("1) Swordsmen ___",sum(swmen),"cost = silver-",swmensc," food-",swmenfc)
    print("2) Archer __",sum(sling),"cost = silver-",slingsc," food-",slingfc)
    print("3) Calvary __",sum(calvmen),"cost = silver-",calvmensc,"food-",calvmenfc)
    print("4) Battering Ram __",sum(batram),"cost = silver-",batramsc,"food-",batramfc)
    sw = int(input("Enter # of Swordsmen: "))
    sl = int(input("Enter # of Archer: "))
    ca = int(input("Enter # of Calvary: "))
    br = int(input("Enter # of Battering Ram: "))
    addingtroops(sw,sl,ca,br)
##----------------------------------------------------------------------------------------------------------------------
def addingtroops(sw,sl,ca,br):
    swfc = swmenfc * sw
    swsc = swmensc * sw
    swmen.append(sw)

    slfc = slingfc * sl
    slsc = slingsc * sl
    sling.append(sl)

    cafc = calvmenfc * ca
    casc = calvmensc * ca
    calvmen.append(ca)

    brfc = batramfc * br
    brsc = batramsc * br
    batram.append(br)

    totalfc = swfc + slfc + cafc + brfc
    c = sum(totalfc)
    food.append(c * -1)
    totalsc = swsc + slsc + casc + brsc
    x = sum(totalsc)
    silver.append(x * -1)

    print("Total Resources spent: Sliver:",sum(totalsc),"Food:",sum(totalfc))
    print("Troops have been trained...")



##----------------------------------------------------------------------------------------------------------------------
def academyR():
    while True:
        print("academyR")
        print("____________________________ACADEMY____________________________")
        print("[TROOP HEALTH",sum(healthlv),"]---[TROOP ATTACK",sum(attacklv),"]---[CONSTRUCTION",sum(constlv),"]")
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("1) upgrade troops health")
        print("2) upgrade troop attack")
        print("3) upgrade construction efficiency")
        print("4) Exit Academy")
        research = input("Enter the number that corresponds with your desired command: ")
        if research == "1":
            print("Troop Heath upgrade cost: Silver:",sum(healthcosts),"Food:",sum(healthcostf))
            f = sum(food)
            hf = sum(healthcostf)
            s = sum(silver)
            hs = sum(healthcosts)
            if f >= hf and s >= hs:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    healthlv.append(1)
                    healthcostf.append(hf)
                    food.append(hf*-1)
                    healthcosts.append(hs)
                    silver.append(hs*-1)
                    print("troop heath upgraded...")
                else:
                    print("no upgrade was made...")
            else:
                print("The are not enough resources for this upgrade...")

        if research == "2":
            print("Troop Attack upgrade cost: Silver:",sum(attackcosts),"Food:",sum(attackcostf))
            f = sum(food)
            hf = sum(attackcostf)
            s = sum(silver)
            hs = sum(attackcosts)
            if f >= hf and s >= hs:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    attacklv.append(1)
                    attackcostf.append(hf)
                    attackcosts.append(hs)
                    food.append(hf*-1)
                    silver.append(hs*-1)
                    print("troop attack upgraded...")

                else:
                    print("no upgrade was made...")
            else:
                print("The are not enough resources for this upgrade...")

        if research == "3":
            print("Construction upgrade cost: Silver:",sum(constcosts),"Food:",sum(constcostf))
            f = sum(food)
            hf = sum(constcostf)
            s = sum(silver)
            hs = sum(constcosts)
            if f >= hf and s >= hs:
                upgrade = input("press (u) to upgrade: ")
                if upgrade == "u":
                    constlv.append(1)
                    constcostf.append(hf)
                    constcosts.append(hs)
                    food.append(hf*-1)
                    silver.append(hs*-1)
                    print("Construction upgraded...")
                else:
                    print("no upgrade was made...")
            else:
                print("The are not enough resources for this upgrade...")
        if research == "4":
            print("exiting academy...")
            break
        else:
            print("currently not an option...")


##----------------------------------------------------------------------------------------------------------------------
def overview():
    print("overview")
    print("Farm-lv",sum(farmlv),"Production-",sum(farmp))
    print("Bank-lv",sum(banklv),"Production-",sum(bankP))
    print("STRONGHOLD-lv",sum(SHlv))
    print("Academy-lv",sum(acadlv))
    print("Barracks-lv",sum(barklv))
    print("Total Resources")
    print("Food-",sum(food))
    print("Silver-",sum(silver))
    print("Total Troops")
    print("Swordsmen-",sum(swmen))
    print("Sligers-",sum(sling))
    print("Calvarymen-",sum(calvmen))
    print("Battering Ram-",sum(batram))
    back = input("Press ENTER to return to base menu")
    if back:
        print("leaving overview")

##----------------------------------------------------------------------------------------------------------------------
def attack(lv):
    print("attack")
    cont = "0"
    while cont != "1":
        s = random.randint(4,30)
        a = random.randint(3,25)
        c = random.randint(2,15)
        b = random.randint(1,10)
        warlootf = random.randint(1000,50000)
        warloots = random.randint(500,10000)
        print("Prepare for battle!")
        time.sleep(2)
        print("sending scout...")
        hey()
        time.sleep(6)
        print(username,"'s TROOPS")
        print("TOTAL TROOPS:",sum(swmen)+sum(sling)+sum(calvmen)+sum(batram))
        print("Swordsmen:",sum(swmen),"Archers:",sum(sling),"Calvary:",sum(calvmen),"Battering Ram:",sum(batram))
        print("----------------------------------VS-----------------------------------------")
        print("ENEMY FORTRESS TROOPS LV",lv)
        print("TOTAL TROOPS:",(s*lv)+(a*lv)+(c*lv)+(b*lv))
        print("Swordsmen:",s*lv,"Archers:",a*lv,"Calvary:",c*lv,"Battering Ram:",b*lv)
        print("WARLOOT:  SILVER:",warloots*lv,", FOOD:",warlootf*lv)
        cont = input("Press ENTER to attack!\nPress (1) to retreat back to base: ")
        if cont == "1":
            print("Swordsmen: 'RETREAT!!'")
        else:
            print("Swordsmen: 'ATTAAACK!!!'")
            time.sleep(3)
            results(s*lv,a*lv,c*lv,b*lv,warloots*lv,warlootf*lv,lv)
        print("\n-\n")

##----------------------------------------------------------------------------------------------------------------------
def results(s,a,c,b,l,f,lv):
    magcount = 0
    slost = (s-swlv1*lv)* -1
    alost = (a-sllv1*lv)* -1
    clost = (c-calv1*lv)* -1
    blost = (b-brlv1*lv)* -1
    ss = sum(swmen)
    aa = sum(sling)
    cc = sum(calvmen)
    bb = sum(batram)
    if ss > s:
        magcount +=1
        swmen.append(slost)
        deaths.append(slost)
        kills.append(s)
    if aa > a:
        magcount +=1
        sling.append(alost)
        deaths.append(alost)
        kills.append(a)
    if cc > c:
        magcount +=1
        calvmen.append(clost)
        deaths.append(clost)
        kills.append(c)
    if bb > b:
        magcount +=1
        batram.append(blost)
        deaths.append(blost)
        kills.append(b)

    if magcount <=1:
        result = "YOU LOST"
        foodwon = 50
        totallootf.append(foodwon)
        silverwon = 25
        totalloots.append(silverwon)
        losses.append(1)

    if magcount == 2:
        result = "DRAW..."
        foodwon = .5*(f)
        totallootf.append(foodwon)
        silverwon = .5*(l)
        totalloots.append(silverwon)
        draws.append(1)

    if magcount == 3:
        result = "VICTORY...YOU WON!"
        foodwon = f
        totallootf.append(foodwon)
        silverwon = l
        totalloots.append(silverwon)
        victory.append(1)

    if magcount == 4:
        result = "GLORIOUS VICTORY!!! YOU COMPLETELY ANNIHILATED THE ENEMY"
        foodwon = 1.5*(f)
        totallootf.append(foodwon)
        silverwon = 1.5*(l)
        totalloots.append(silverwon)
        victory.append(1)
        gloriousv.append(1)
    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~~~~BATTLE RESULTS~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print("``````````",result,"``````````````")
    time.sleep(2)
    print("FOOD WON:",foodwon,"SILVER WON",silverwon)
    time.sleep(1)
    print("TROOPS LOST: Swordsmen:",slost,"Archers:",alost,"Calvary:",clost,"Battering Ram:",blost)
    print("<^><^><^><^><^>|||||||||||||||||||||||||||||||||||||||||||||||<^><^><^><^><^><^><^><^>")
    print("")
    time.sleep(3)
    food.append(foodwon)
    silver.append(silverwon)


##----------------------------------------------------------------------------------------------------------------------
def hey():
    c = random.randint(0,3)
    if c == 0:
        print("Swordsmen: 'we can take these bastards!'")
    elif c == 1:
        print("Archer: 'Aim high boys!'")
    elif c == 2:
        print("Calvary: 'Get mounted men! And wait for my signal'")
    elif c == 3:
        print("Battering Ram: 'Must... keep... fighting...'")



##----------------------------------------------------------------------------------------------------------------------
def statsheet():
    c = sum(victory)
    d = sum(draws)
    l = sum(losses)
    totalfought = c+d+l
    winp = c/totalfought * 100
    print(".......................................stat-sheet.....................................")
    overview()
    print("BATTLES WON:",sum(victory))
    print("BATTLES WON GLORIOUSLY:",sum(gloriousv))
    print("BATTLE DRAWS:",sum(draws))
    print("BATTLES LOST:",sum(losses))
    print("ENEMY TROOP KILLS:",sum(kills))
    print("TROOP DEATHS:",sum(deaths))
    print("WIN PERCENTAGE:",winp,"%")
    print(",`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,`")
    time.sleep(15)
##----------------------------------------------------------------------------------------------------------------------
def main():
    userinfo()
    intropage()
    statsheet()

main()
