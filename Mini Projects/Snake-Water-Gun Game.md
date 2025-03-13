Summary of the Snake-Water-Gun Game Program
This Python program is a Snake-Water-Gun game, a variation of Rock-Paper-Scissors. The user plays against the computer, and the game continues until the player decides to stop. The program keeps track of scores and announces the winner at the end.

How the Program Works
1️⃣ Displaying Game Rules
When the program starts, it prints an introduction explaining the rules:

Snake (🐍) vs. Water (💦) → Snake wins
Gun (🔫) vs. Snake (🐍) → Gun wins
Water (💦) vs. Gun (🔫) → Water wins
Same choices → Draw
It also describes the scoring system:

Win = +1 point
Loss = 0 points
Draw = No points
2️⃣ Game Loop: User & Computer Choices
The game runs inside a while True loop, allowing multiple rounds.
The user enters their choice (S, W, or G).
The computer randomly selects a choice (S, W, or G) using random.choice().
The program checks who wins the round based on the game rules.
3️⃣ Determining the Winner
The program defines helper functions to:

Convert the computer’s choice (s, w, g) to full words (comp_words()).
Convert the user’s choice (s, w, g) to full words (user_words()).
Print both user and computer choices (final_words()).
Announce the final winner (points()).
The program then checks for:

Draw → If both choices are the same.
Win/Loss Conditions → Based on the game rules, the winner gets +1 point.
4️⃣ Asking to Play Again
After each round, the user is asked:
"Do you want to play again? (Y/N)"
If the user types "Y", the game restarts.
If "N", the program displays the final scores and declares the overall winner.


Final Output Example

------------------------------------------------------
|| Snake-Water-Gun Game Rules 🐍💦🔫 ||
------------------------------------------------------
Snake (🐍) drinks Water (💦) → Snake wins
Gun (🔫) kills Snake (🐍) → Gun wins
Water (💦) rusts Gun (🔫) → Water wins
Same choices → Draw
------------------------------------------------------
|| Scoring System ||
- Win = +1 point  
- Lose = 0 points  
- Draw = No points  
------------------------------------------------------

Enter your choice (Snake[S], Water[W], Gun[G]): S
User choose: Snake || Computer Choose: Water
You Win!

Do you want to play again? (Y/N): Y
...
Final Score:
Your Score: 3 | Computer Score: 2
You win !!
Thanks for playing! 👋
