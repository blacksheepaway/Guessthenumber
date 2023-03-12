<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Guess The Number Game</h1>
    <p>Welcome to the Guess The Number game! This program is a simple game in which the user has to guess a number between 1 and 10, and the computer will generate a random number as well. If the user guesses the number correctly, they win the game! If not, they lose.</p>
    <h2>How it works</h2>
    <p>The game begins by displaying the title in ASCII art format using the Python <code>print()</code> function. After that, the user is prompted to enter a number between 1 and 10. The <code>input()</code> function is used to get the user's input, which is then converted to a float using the <code>float()</code> function.</p>
    <p>The program then generates a random number between 1 and 10 using the <code>random.randint()</code> function. The user's input and the computer's random number are then compared using an <code>if</code> statement.</p>
    <p>If the two numbers are the same, the user wins the game and a message is displayed to inform them. Otherwise, the user loses the game and a message is displayed to inform them.</p>
    <p>After each round, the user is prompted to play again. If they choose to play again, the game continues. If not, the program thanks the user for playing and exits.</p>
    <h2>Techniques Used</h2>
<p>This program was written in Python and showcases several key techniques to create a fun and engaging game for the user. Here are a few of the techniques used:</p>
<ul>
  <li><strong>Random number generation:</strong> The program uses Python's built-in random module to generate a random number between 1 and 10 for the computer's choice in the game. This ensures that each game is unique and unpredictable.</li>
  <li><strong>User input:</strong> The program prompts the user to enter a number between 1 and 10 as their guess in the game. The user's input is stored as a float data type and used to determine the outcome of the game.</li>
  <li><strong>Conditional statements:</strong> The program uses if/else statements to determine whether the user has won or lost the game based on their guess and the computer's choice.</li>
  <li><strong>String formatting:</strong> The program uses Python's f-string formatting capabilities to display the user's guess and the computer's choice in the output message. This provides a clear and concise display of the game results to the user.</li>
</ul>
<p>These techniques demonstrate the power and versatility of Python programming and showcase the author's proficiency in the language.</p>
    <h2>Example Output</h2>
    <p>Here's an example output of the program:</p>
    <pre>
 _____                     _   _                                         
/ ____|                   | | (_)                                        
| |  __ _   _  ___  ___ ___| |_ _  ___  _ __                              
| | |_ | | | |/ _ \/ __/ __| __| |/ _ \| '_ \                             
| |__| | |_| |  __/\__ \__ \ |_| | (_) | | | |                            
\_____|\__,_|\___||___/___/\__|_|\___/|_| |_|                                                         

Enter a number from 1 to 10: 5
Your number is 5 and the computer chose 8. You lost!
Do you want to play again? (y/n): y

Enter a number from 1 to 10: 3
Your number is 3 and the computer chose 3. You won!
Do you want to play again? (y/n): n

Thanks for playing!
</pre>
<h2>Contributing</h2>
<p>If you'd like to contribute to this project, please fork the repository and submit a pull request.</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE.md">
