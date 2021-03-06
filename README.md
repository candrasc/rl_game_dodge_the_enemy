# rl_game_dodge_the_enemy

## Game Objectives:
1) Collect all the rewards (multi-color bouncing squares)
2) Dodge the enemies (red bouncing squares)

## See it in action! ##
### Below is the RL agent beating a simplified version of the game where all objects are the same size 

![alt text](https://github.com/candrasc/rl_game_dodge_the_enemy/blob/main/read_me_images/ezgif-2-b3433a7c00d1.gif "RL Agent Victory")

I created a game from scratch with the purpose of teaching a reinforcement learning agent to play it. The core of the game is the environment class that sets what is possible within its boundries and allows the objects within it to act in a certain way. I also created object classes which interact within the environment (Players, Enemeis, Rewards). Its mostly a lot of numpy and rendered with Pygame!  Game.py is then a series of functions to have the environment step in a way that easily interacts with pygame. 

This game can be played by a player or a reinforcement learning agent. You can run main.py to play yourself, and main_rl.py to watch an rl agent play. Double tap "spacebar" to play the exact some environment that you just died on (or won), and double tap "q" to randomly create a new environment within the bounds you specified in the config.json.

The RL agent has been able to succesfully win an easier version of the game you can see below. In the near future, I will write an article about the methodology and "tricks" I used to get the agent to learn the game. This agent is far from perfect and will be updated to more advanced algorithms such as actor-critic.

A lot of the work getting the RL agent to work is found in the StateTranslator class. This takes the positions returned by the environment at each step, and transforms them into rich features for the agent to learn at a much faster rate. 






