import random


o = ["rock","paper","scissor"]

cpo = 0
upo = 0

while True:
    ch = input("choose rock/paper/scissor or q to exit:  ")
    ch = ch.lower()
    
    if ch == "q":
        break
    if ch not in o:
        print("please choose the options wisely...!")
        continue

    cum_n = random.randint(0,2)
    cum_o = o[cum_n]
    print(f"computer picked {cum_o}")

    if cum_o == ch:
        print("Tie ")
        
    elif cum_o == "rock" and ch == "paper":
        print("won ")
        upo += 1

    elif cum_o == "paper" and ch == "scissor":
        print("won ")
        upo += 1
        
    elif cum_o == "scissor" and ch == "rock":
        print("won ")
        upo += 1
    else:
        print("lose ")
        cpo += 1


print("you have scored", upo)
print("computer scored", cpo)
