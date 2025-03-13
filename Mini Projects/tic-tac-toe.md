**Summary of the Program**

This Python program is a command-line-based game similar to Tic-Tac-Toe. It allows a player to compete against a computer in a grid-based game. The program offers three difficulty modes and follows different win conditions based on the selected mode. The game continues until a player wins, the board is full, or the user chooses to exit or restart.

---

**How the Program Works**

### 1. **Displaying the Rules**
   - At the start, the game prints the rules in a formatted table.
   - The player is prompted to choose their symbol, and a symbol for the computer is also selected.
   
### 2. **Choosing the Difficulty Mode**
   - The user selects a mode:
     - **Easy Mode:** Standard Tic-Tac-Toe rules apply.
     - **Medium Mode:** If no one wins, the player is declared the winner.
     - **Hard Mode:** If the computer wins, the player is still declared the winner.
   - If an invalid input is entered, the program prompts the user to enter a valid choice.

### 3. **Game Board Representation**
   - The board is displayed using numbers 1-9 to represent positions.
   - Players take turns choosing positions.

### 4. **Game Logic Execution**
   - The game starts once the user presses enter.
   - The player selects a position from the board.
   - The position is checked for availability before updating.
   - The computer then selects a random available position.
   - The board updates and displays after each move.

### 5. **Win Conditions**
   - The program checks if either the player or computer has won using predefined winning conditions.
   - If there is a winner, the program displays the result based on the chosen mode:
     - Victory emojis and messages are displayed accordingly.
   - If the board is full and no one wins, it is a draw.

### 6. **Replay and Exit Options**
   - After a round, the player can choose to:
     - Exit the game.
     - Replay with the same settings.
     - Change the mode.
     - Change symbols.
   - The board resets if a replay is chosen.

### **Key Features of the Game**
- User-friendly interface with clear instructions.
- Multiple game modes for varied difficulty.
- Ensures valid user input to avoid errors.
- Randomized computer moves for an unpredictable experience.
- Allows users to restart or change settings without restarting the program manually.

This game is a fun and engaging way to play a simple strategy-based challenge against an AI opponent. The different modes introduce a unique twist, making it more interesting than a traditional Tic-Tac-Toe game.

