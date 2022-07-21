import random
options=['Rock','Paper','Scissors']
scors={'user':0,'computer':0}
n=int(input("How many times do you want to play?"))

for i in range(n):
    Computer_choice=random.choice(options)
    User_choice=input("Choose an option: ")
    
    print("Compute choice=", Computer_choice)
    if User_choice=='Rock' and Computer_choice=='Paper':
        print("Computer wins!")
        scors['computer'] += 1
    elif User_choice=='Rock' and Computer_choice=='Scissors':
        print("You win!")
        scors['user'] += 1
    elif User_choice=='Paper' and Computer_choice=='Rock':
        print("You win!")
        scors['user'] += 1
    elif User_choice=='Paper' and Computer_choice=='Scissors':
        print("Computer wins!")
        scors['computer'] += 1
    elif User_choice=='Scissors' and Computer_choice=='Rock':
        print("Computer wins!")
        scors['computer'] += 1
    elif User_choice=='Scissors' and Computer_choice=='Paper':
        print("You win!")
        scors['user'] += 1
    elif User_choice==Computer_choice:
        print("Draw")       

print("Your Score=", scors['user'])
print("Computer Score=", scors['computer'])
        
if scors['computer'] > scors['user']:
    print("Winner of the game: Computer")
elif scors['computer']==scors['user']:
    print("Draw!")
else:
    print("Winner of the game: You")