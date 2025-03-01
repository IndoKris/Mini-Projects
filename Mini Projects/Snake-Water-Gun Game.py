
import random 
print('''
------------------------------------------------------
|| Snake-Water-Gun Game Rules 🐍💦🔫 ||
------------------------------------------------------
Snake-Water-Gun is a simple hand game , where:
Snake (🐍) drinks Water (💦) → Snake wins
Gun (🔫) kills Snake (🐍) → Gun wins
Water (💦) rusts Gun (🔫) → Water wins
Same choices → Draw
------------------------------------------------------
|| Scoring System ||
- Win = +1 point  
- Lose = 0 points  
- Draw = No points  
- One with the most points wins the game.
------------------------------------------------------

''')
user_points = comp_points = 0
while True :

    user_choice = (input("Enter your choice (Snake[S], Water[W], Gun[G]) : ")).strip().lower()

    choice = user_choice[0]
    
    Comp_choice = random.choice(["s", "w", "g"])

    def comp_words():
        """Returns the full word for the computer's choice"""
        if Comp_choice == 's':
            return "Snake"
        elif Comp_choice == 'w':
            return "Water"
        elif Comp_choice == 'g':
            return "Gun"
    # comp_words(Comp_choice)


    def user_words():
        """Returns the full word for the user's choice"""
        if choice == 's':
            return "Snake"
        elif choice == 'w':
            return "Water"
        elif choice == 'g':
            return "Gun"
        
    # user_words(user_choice)

    def final_words():
        print(f"User choose : {user_words()} || Computer Choose : {comp_words()}")


    def points():
        if(comp_points>user_points):
            print("Computer Wins !")
        elif (comp_points==user_points):
            print("Its a Draw ")
        elif (comp_points<user_points):
            print("You win !! ")
    

    if (Comp_choice==choice):
        print("Its a Draw")
        final_words()
    else :
        if(Comp_choice== "s" and choice== "w" ):
            print("Computer Wins !")
            final_words()
            comp_points += 1
            
        elif(Comp_choice== "s" and choice== "g" ):
            print("You Win !")
            final_words()
            user_points += 1
        
        elif(Comp_choice== "g" and choice== "s" ):
            print("Computer Wins !")
            final_words()
            comp_points += 1

        elif(Comp_choice== "g" and choice== "w" ):
            print("You Win !")
            final_words()
            user_points += 1
        
        elif(Comp_choice== "w" and choice== "s" ):
            print("You Win !")
            final_words()
            user_points += 1
        
        elif(Comp_choice== "w" and choice== "g" ):
            print("Computer Wins !")
            final_words()
            comp_points += 1
        
        else :
            print("Something went wrong !")


    
    play_again = input("Do you want to play again ? (Y/N)").strip().lower()
    if play_again != "y":
        print("Final Score:")
        print(f"Your Score : {user_points} | Computer Score : {comp_points}")
        points()
        print("Thanks for playing! 👋")
        break

