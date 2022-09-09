saras=input()
kushi=input()

if saras==kushi:
    print("Tie")
elif  saras=="rock" and kushi=="paper":
    print("kushi wins")
elif  saras=="scisors" and kushi=="rock":
    print("kushi wins")
elif  saras=="paper" and kushi=="scisors":
    print("kushi wins")
elif  saras=="rock" and kushi=="scisors":
    print("saras wins")
elif  saras=="scisors" and kushi=="paper":
    print("saras wins")
elif  saras=="paper" and kushi=="rock":
    print("saras wins")
    


