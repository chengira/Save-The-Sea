:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
#  Save the Sea 
## CS 110 Final Project
###  Fall, 2021 
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://github.com/bucs110a0fall21/final-project-the-boy-friends

<< [link to demo presentation slides](#) >>

### Team:  The Boyfriends 
####  Chao Lin, Carl Huang, Ira Cheng

***

## Project Description *(Software Lead)*
<< This is a project that emulates a space invader game with asteroids, but with a twist as the concept is based on destroying garbage cans that are falling into Earth's oceans. The player plays as a fighter jet that they can control using keyboard inputs. The objective is to evade the garbage cans while using the fighter jet to destroy any that get in the way. The player should try to score as many points as possible without draining their health bar. As the gameplay progresses, the odds of the player's survivability decreases. >>

***    

## User Interface Design *(Front End Specialist)*
* ![game](assets/game)
  ![start_screen](assets/start_screen)
  ![game_over](assets/game_over) 
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * ![class diagram](assets/diagram)
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. Weapon, Ship, Monster >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * controller.py
    * monster.py
    * ship.py
    * weapon.py
* assets
    * laser.png
    * class_diagram.jpg
    * trash(2).png
    * jet(3).png
    * ocean.png
    * Start_song.wav
    * Game_song.wav
    * End_song.wav
    * diagram
    * game
    * game_over
    * start_screen
* etc
    * Scores.json

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Ira Cheng

<< Worked as integration specialist by... >>

### Front End Specialist - Carl Huang

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Chao Lin

<< The back end specialist... >>

## Testing *(Software Lead)*
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Open the terminal of the machine, navigate to folder, and type into terminal \u201cpython3 main.py\u201d. | 1) The program starts and the player is presented with the main menu screen. 2) Player is greeted with a soundtrack. |         |
|  2  | Click \u201cExit Game\u201d button | 1) All aspects of the program ceases to operate and the player returns to step 1. |          |
|  3  | Click \u201cStart Game\u201d button | 1) The program progresses from the main menu screen to the gameplay screen. 2) Music switches to a more dramatic beat 3) Monsters instantly spawn from the top of the screen |          |
|  4  | Press LEFT ARROW, hold LEFT ARROW | 1) The ship which the player is now controlling will shift one time to the left side of the screen if the left arrow is pressed. 2) The ship which the player is now controlling will move continuously to the left side of the screen if the left arrow is held. 3) If the ship reaches a point left enough it will no longer move left. |         |
|  5  | Press RIGHT ARROW, hold RIGHT ARROW | 1) The ship which the player is now controlling will shift one time to the right side of the screen if the right arrow is pressed. 2) The ship which the player is now controlling will move continuously to the right side of the screen if the right arrow is held. 3) If the ship reaches a point right enough it will no longer move right. |          |
|  6  | Press SPACE BAR | 1) The ship which the player controls will fire a cannon ball in front which will travel to the top of the screen and disappear unless it makes contact with an object such as a monster, in which case it will disappear and deal damage to the monster. |           |
|  7  | General Gameplay | 1) The ship moves properly from left to right of the screen responsively and does not move outside of the screen. 2) The cannon balls are shot from the ship and travel in a straight line and defeat the incoming creatures. 3) Score on the top of the screen increases as the player eliminates more monsters. 4) Game becomes increasingly difficult as the time the player survives increases. 5) Player\u2019s health bar decreases consistently as ship collides with monsters and loses when the bar goes all the way down. |             |
|  8  | Force fail state | 1) Occurs when the user loses all of their health in the health bar. 2) Gameplay stops and transfers to a game over screen which displays \u201cGame Over.\u201d 3) Sad music plays 4) The score that the player obtained for that run is displayed and under which is the high score. If a high score is reached, the score \u201cNew Highscore!\u201d will be displayed. Scores are saved in a separate file and updated with new high score. |             |
|  9  | Testing each button on the fail state screen | 1) The \u201cPlay Again\u201d button restarts the game with no glitches and issues. 2) The \u201cExit\u201d button quits the program and the entirety of the program terminates. |             |
|  10  | Click the \u201cX\u201d button on the top right corner of the window. | 1) The game closes properly with the entirety of the program terminating. |           |



 


















