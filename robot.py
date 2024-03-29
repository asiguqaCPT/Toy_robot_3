"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""

# list of valid command names
valid_commands = ['replay','off', 'help', 'forward', 'back', 'right', 'left', 'sprint']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# Variable to keep track of commands
command_list = []

# Variable for non movement commands
non_movement = ['off','help']
replay = ['silent','reversed','reversed silent']

def update_c_history(e_command):
    global command_list
    command_list.append(e_command)


def retrieve_commands():
    return command_list


def do_replay(robot_name, n_replays):
    global command_list
    int_1 = n_replays[0]
    int_2 = n_replays[1]

    r_commands = [i for i in command_list if i not in non_movement and not i.startswith('replay')]
    if int_1 == 0 and int_2 == '': 
        for i in r_commands:
            handle_command(robot_name, i)
    elif int_1 != 0 and int_2  == '':
        r_commands = r_commands[-int_1:]
        for i in r_commands:
            handle_command(robot_name, i)
    elif int_2 != '':
        r_commands = r_commands[-int_1:-int_2]
        for i in r_commands:
            handle_command(robot_name, i)
        pass
    return True,' > ' + robot_name + ' replayed ' + str(len(r_commands)) + ' commands.'
        

def do_replay_reversed(robot_name, n_replays):
    global command_list
    int_1 = n_replays[0]
    int_2 = n_replays[1]
    r_commands = [i for i in command_list if i not in non_movement and not i.startswith('replay')]
    r_commands.reverse()
    
    if int_1 == 0 and int_2 == '':
        for i in r_commands:
            handle_command(robot_name, i)
    elif int_1 != 0 and int_2 == '':
        r_commands = r_commands[-int_1:]
        for i in r_commands:
            handle_command(robot_name, i)
    elif int_2 != '':
        r_commands = r_commands[-int_1:-int_2]
        for i in r_commands:
            handle_command(robot_name, i)
    return True,' > ' + robot_name + ' replayed ' + str(len(r_commands)) + ' commands in reverse.'


def do_replay_reversed_silent(robot_name, n_replays):
    global command_list
    r_commands = [i for i in command_list if i not in non_movement and not i.startswith('replay')]
    r_commands.reverse()
    
    int_1 = n_replays[0]
    int_2 = n_replays[1]
    if int_1 == 0 and int_2 =='':
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif int_1 != 0 and int_2 == '':
        r_commands = r_commands[-int_1:]
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                    (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                    (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                    (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                    (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif int_2 != '':
        r_commands = r_commands[-int_1:-int_2]
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                (do_next, command_output) = do_sprint(robot_name, int(arg))

    return True,' > ' +  robot_name + ' replayed ' + str(len(r_commands)) + ' commands in reverse silently.'


def do_replay_silent(robot_name, n_replays):
    global command_list
    r_commands = [i for i in command_list if i not in non_movement and not i.startswith('replay')]
    '''
    for i in r_commands:
        (command_name, arg) = split_command_input(i)   
        if command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg)) 
    '''
    int_1 = n_replays[0]
    int_2 = n_replays[1]
    if int_1 == 0 and int_2 =='':
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif int_1 != 0 and int_2 == '':
        r_commands = r_commands[-int_1:]
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                    (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                    (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                    (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                    (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif int_2 != '':
        r_commands = r_commands[-int_1:-int_2]
        for i in r_commands:
            (command_name, arg) = split_command_input(i)
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
            elif command_name == 'back':
                (do_next, command_output) = do_back(robot_name, int(arg))
            elif command_name == 'right':
                (do_next, command_output) = do_right_turn(robot_name)
            elif command_name == 'left':
                (do_next, command_output) = do_left_turn(robot_name)
            elif command_name == 'sprint':
                (do_next, command_output) = do_sprint(robot_name, int(arg))

    return True,' > ' +  robot_name + ' replayed ' + str(len(r_commands)) + ' commands silently.'


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name
    

def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
        
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)   
    
    update_c_history(command.lower())
    return command.lower()
    

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''
    

def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def valid_range(c_range): #checks that the range is of the input formmrt a-b
    if '-' in c_range:
        int_1 = c_range[:c_range.index('-')]
        int_2 = c_range[c_range.index('-')+1:]
        if is_int(int_1) and is_int(int_2):
            return True
    else:
        return False


def number_of_replays(command): #calculate the range of commands to replay
    n_replay = command.split(' ')
    (command_name, arg1) = split_command_input(command)
    if command_name == 'replay' and arg1 in replay or len(arg1) == 0:
        return 0,''
    elif command.startswith('replay') and is_int(n_replay[1]):
        return int(n_replay[1]),''
    elif command.startswith('replay') and '-' in n_replay[1]:
        r = tuple(n_replay[1].split('-'))
        r = int(r[0]), int(r[1])
        return r 


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """   
    move = ['forward','back','sprint']
    assist = ['off','help','right','left']
    command = command.lower().strip()
    (command_name, arg1) = split_command_input(command) 
    args = arg1.split(' ',1)
    n_commands = command.split(' ')
    if command_name == 'replay' and (arg1 in replay or is_int(arg1) or valid_range(arg1) or len(arg1) == 0):
            return True
    elif command_name in move and is_int(arg1):
            return True
    elif command_name in assist and arg1 == '':
        return True
    elif command_name == 'replay' and is_int(args[0]) or valid_range(args[0])  and args[1] in replay:
        return True
    else:
        return False
    
    
def output(name, message):
    print(''+name+": "+message)
    
    
def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
REPLAY - replay 'movement' commands, 
    i.e replay (replays all commands)
    optional flag to specify number/range of commands to replay
    i.e replay 4 or replay 4-2 (replay with optional flags)
REPLAY SILENT - replay without showing output for each command
    i.e replay silent (silently replays all commands)
    with optional flags to specify number/range of commands to replay silently
    i.e replay 2 silent or replay 3-1 silent
REPLAY REVERSED - replay the commands in reverse order
    i.e replay reversed (replay all comands in reverse)
    with optional flags to specify number/range of commands to play in reverse
    i.e replay 2 reversed or replay 2-1 reversed
REPLAY REVERSED SILENT - replay reversed, but only output number of commands and final position
    i.e replay reversed silent (replays all commands in reversed silently)
    with optional flags to specify number/range of commands to replay in reverse silently
    i.e replay 2 reversed silent or replay 4-2 reversed silent
SPRINT - sprint forward by specified number of steps i.e sprint 5
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    
    
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """    
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """    
    
    global position_x, position_y
    new_x = position_x
    new_y = position_y  
    
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps    
    
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False
    

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """ 
    
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index    
    
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0    
    
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index 
    
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3    
    
    return True, ' > '+robot_name+' turned left.'
        

def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """    
    
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """    
    
    (command_name, arg) = split_command_input(command.strip())
    replay_range = number_of_replays(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg)) 
    elif 'reversed silent' in arg:
        (do_next, command_output) = do_replay_reversed_silent(robot_name, replay_range)
    elif 'silent' in arg: 
        (do_next, command_output) = do_replay_silent(robot_name, replay_range)
    elif 'reversed' in arg:
        (do_next, command_output) = do_replay_reversed(robot_name, replay_range)
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(robot_name, replay_range)
    
    print(command_output)
    show_position(robot_name)
    return do_next
    

def robot_start():
    """This is the entry point for starting my robot"""  
    global position_x, position_y, current_direction_index    
    global command_list 
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!") 
    
    position_x = 0
    position_y = 0
    current_direction_index = 0
    command_list = []    
    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
