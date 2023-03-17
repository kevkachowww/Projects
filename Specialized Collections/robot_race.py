'''
The Great Robot Race

The brushless motors are roaring, and the race is about to begin! In this project,
we will be using some of the advanced containers in Python to command, track,
and score simple robots which are trying to traverse different mazes. Your job will be to fill in the missing code
from the robot_race.py file. A lot of background code has been provided in the robot_race_functions.py file
which we will be using, but the primary focus of this project is to use advanced collections in a meaningful way.
'''

import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
  # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
  # Add your code below!
  for bot in bots:
    if not bot.has_finished:
      robot_moves.append(rr.compute_robot_logic(walls, goal, bot))

  num_of_turns += 1

# Count the number of moves based on the robot names
# Add your code below!
moveCount = Counter(move[0] for move in robot_moves)

# Count the number of collisions by robot name
# Add your code below!
collisionCount = Counter(move[0] for move in robot_moves if move[2])

# Create a namedtuple to keep track of our robots' points
# Add your code below!
BotScoreData = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])

# Calculate the scores (moves + collisions) for each robot and append it to bot_scores
bot_scores = []
# Add your code below!
for bot in bots:
  bot_scores.append(BotScoreData(bot.name, moveCount[bot.name], collisionCount[bot.name], moveCount[bot.name]+collisionCount[bot.name]))

# Populate a dict to keep track of the robot movements
bot_data = {}
# Add your code below!
for bot in bots:
  bot_data[bot.name] = bot


# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
  # Make sure to pop moves from the front of the deque
  # Add your code below!
  move = robot_moves.popleft()
  bot_data[move[0]].process_move(move[1])

  # Update the maze characters based on the robot positions and print it to the console
  rr.update_maze_characters(maze_data, bots)
  rr.print_maze(maze_data)
  sleep(seconds_between_turns - time() % seconds_between_turns)

# Print out the results!
rr.print_results(bot_scores)