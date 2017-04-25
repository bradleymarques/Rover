Rover is a simple navigation module, which accepts a three-line list of commands and returns the location of the Mars Rover after the execution of these commands.
The command list format is as follows:

 zone_width zone_height
 x_coord y_coord direction
 movement_and_rotation_sequence

where

- zone_width, zone_height, x_coord, y_coord are integers and represent correspondingly the width and height of the zone of travel and the x and y coordinate of the starting position within the zone.
- direction is one of the letters E,N,W,S that correspond to the Rover's orientation towards East, North, West,or South.
- movement_and_rotation_sequence is a string sequence of 'M','L', and 'R' corresponding to 1-point move, 90-degrees' rotation left, and 90-degrees' rotation right.

An example of the command list:
8 8
1 2 E
MMLMRMMRRMML


DESIGN
The main logic of the module is in Rover.location function. This function accepts the command list as three arguments, corresponding to the command list's line: dimensions, position, movement. This allows to easily call the function from tests.
The inputs for Rover.py can be specified in two ways:
1. Inputs could be read from input.txt file in the working directory. An example input.txt is provided.
2. Inputs can be specified as runtime arguments: each line of the command list corresponds to one runtime argument. The example command list above should be specified as "8 8" "1 2 E" "MMLMRMMRRMML".
Rover.location uses regular expressions to ensure that the inputs are in the correct format.
Trigonometric functions are used to calculate new coordinates after the move.


EXECUTION
The module requires the interpreter with math, re, and sys modules. The module can be executed from the command-line (make sure that input.txt is in the same directory):
C:\Users\tetya\PycharmProjects\Rover>Rover.py
3 3 S
Alternatively, the module can be executed from the command-line with arguments (no input.txt is required).
C:\Users\tetya\PycharmProjects\Rover>Rover.py "6 7" "3 1 W" "MMMLLMRM"
1 0 S


TESTING
test.py is provided to test the correctness of the navigation and the ability of the module to deal with unexpected or wrong inputs.

