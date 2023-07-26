# Project: Igra Memorija - Memory Game Simulation

## Introduction
This project is developed using the Raspberry Pi Pico microcontroller and MicroPython language, along with a matrix keyboard and TFT SPI display. The main function of this project is to simulate a memory game with different levels of difficulty. Link to a video presentation of the project: https://www.youtube.com/watch?v=S6pZJlPe3G4

## System Description
The system utilizes the Raspberry Pi Pico microcontroller as the central processing unit. A matrix keyboard serves as the input device for user interaction, while a TFT display is used for visualizing the game and the user interface.

## Features
1. Main Menu: At the beginning, the user is presented with a menu containing four options - "Variant A," "Variant B," "Game Info," and "Shut Down."
2. Mode Selection: The user can choose between "Variant A" or "Variant B" to play the game. Additionally, they can select the "Game Info" option to get information about the game rules or shut down the microcontroller by pressing a specific key on the matrix keyboard.
3. Memory Game: When a mode is selected, the user is presented with a screen showing a 3x3 grid and the current level number on the top. The grid displays random sequences of numbers whose size increases with each level. During the display of a sequence, circles are drawn in blue color. When the user enters a number on the matrix keyboard, a green circle is drawn in the corresponding square as confirmation. The user can also delete a previously entered number, and in that case, a red circle is drawn as confirmation of deletion. The user confirms the entered sequence by pressing the "#" button. If the user enters the correct sequence, they proceed to the next level; otherwise, the game automatically restarts from the first level.
4. Variant A: In this mode, a new sequence of random numbers is generated for each level. After a certain level, a timer appears, limiting the user's time to enter the sequence, creating additional pressure that makes it harder for the player to continue successfully. Additionally, the confirmation of the previous entered number (drawing green circles) is disabled.
5. Variant B: In this variant, for each level, the previous part of the sequence remains the same, and only one number is added to the sequence. The trick is that after the 5th level, circles are immediately displayed one after another without waiting, and after the 10th level, circles shrink and appear faster, making it significantly more challenging to advance to the next levels.
6. Game Complexity: As the levels progress, the game becomes more complex - sequence sizes increase, a timer with reduced time for entering the sequence appears, and circles shrink and appear faster.
7. Return to Main Menu: The user can return to the main menu at any time and reselect a mode, get information about the game, or stop the game.

## Technical Specifications
1. Microcontroller: Raspberry Pi Pico
2. Programming Language: MicroPython
3. Input Device: Matrix Keyboard
4. Output Device: TFT Display

## Team Members:
1. Kenan Dizdarević
2. Ali Boudellaa
3. Nedim Hošić
4. Berin Karahodžić

   
## Conclusion
This project offers a simple and intuitive solution for simulating the memory game. By combining hardware components and MicroPython programming, the game provides various levels of challenge to cater to different users' needs.

