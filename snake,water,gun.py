import random
computer=random.choice([1,-1,0])
youchance=input("enter your chance=")
dict={"snake":1,"gun":0,"Water":-1}
reversedict={1:"snake",-1:"water",0:"gun"}
you=dict[youchance]
#sprint=(f"you chose{reversedict[youchance]} computer chose {reversedict[computer]}")


if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win")
         
    elif(computer==-1 and you==0):
        print("you lose")
         
    elif(computer==1 and you==-1):
        print("you lose")
         
    elif(computer==1 and you==0):
        print("you win")
         
    elif(computer==0 and you==1):
        print("you lose")
         
    elif(computer==0 and you==-1):
        print("you win")
    else:
        print("something went wrong")     



       