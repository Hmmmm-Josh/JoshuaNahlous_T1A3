# List of valid commands
valid_commands = ["move", "left", "right", "report", "place"]


# variables tracking position and direction
global position_x, position_y, command_history
command_history = []

position_x = 0
position_y = 0
current_direction_index = 0


# function get's robots name
def get_robot_name():
  name = input("What do you want to name your robot?")
  while len(name) == 0:
    name = input("What do you want to name your robot?")
  return name

#Ask user for a command 
def get_command(robot_name):
  prompt = ''+robot_name+': What must I do next? '
  command = input(prompt)
  while len(command) == 0 or not valid_command(command):
    output(robot_name, "Sorry, I did not understand '"+command+"'.")
  command = input(prompt)
  return command.lower()


def output(name, message):
  print(''+name+": "+message)