import random
random_num = random.random()

def coinTosses(times):
    headcount = 0
    tailscount = 0
    result = ["head!", "tail!"]
    for x in range (0, times):
        thisresult = result[random.randint(0,1)]
        print "Throwing a coin..." + " It's a " + thisresult + " ... " + "Got " + str(headcount) + " heads and " + str(tailscount) + " tails so far."
        if (thisresult == "head!"):
            headcount += 1
        elif (thisresult == "tail!"):
            tailscount += 1



coinTosses(5000)
