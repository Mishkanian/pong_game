# Pong

## Project Overview
The purpose of this project is to create Pong using Python. Pong is a classic 2-D arcade game originally released in 1972 and created by [Allan Alcorn](https://en.wikipedia.org/wiki/Allan_Alcorn). To learn more about the origins of Pong, [click here](https://en.wikipedia.org/wiki/Pong).

![pong_game_image](https://github.com/Mishkanian/pong_game/blob/main/README_images/pong_game.png)


## How to Run this Game
Download [Pong.py](https://github.com/Mishkanian/pong_game/blob/main/Pong.py) from this repository. After downloading this file, run it.

## How to Play
This game requires two players. The objective of the game is to bounce the ball away from your side of the screen using your paddle. If you miss the ball, your opponent scores 1 point.  

The controls for **Player 1** are:  
**w**  - go up  
**s**  - go down

The controls for **Player 2** are:  
**"Up Arrow"**  - go up  
**"Down Arrow"**  - go down

## How to Adjust the Game Difficulty
To increase or decrease the difficulty of the game, open [Pong.py](https://github.com/Mishkanian/pong_game/blob/main/Pong.py) in a code editor (such as [VSCode](https://code.visualstudio.com/)) and change the lines of code found below on lines 37 and 38.

```python
ball.dx = .33 # movement speed of the ball dx
ball.dy = .33 # movement speed of the ball dy
```

Increasing these values will increase the ball speed and therefore make the game more difficult. If the ball is moving too slow, increase these values. However, increasing these values too much will cause the ball to shoot across the screen and now allow the paddles enough time to get to the ball. If the ball is moving too fast, decrease these values.

## Ideas for Future Development
- For future development, I would add sounds to the game. For example, sounds when the ball hits a paddle and when players score points. This would make the experience much more fun and engaging.

- One important feature to implement is a "winning score." Currently, the game does not end!

- I would also create a simple computer opponent to enable a single player mode.

**Author: Michael Mishkanian**  
For all questions and inquiries, please contact me on [LinkedIn](https://www.linkedin.com/in/michaelmishkanian/).
