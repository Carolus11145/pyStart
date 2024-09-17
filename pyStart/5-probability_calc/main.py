import copy # a module containing methods related to copying different lists, objects, arrays, etc.
import random # a module which is composed of methods for generating random nums in various ways

class Hat:
    # Instantiate an instance variable for the contents of the hat along with a dictionary for user inputs
    def __init__(self, **inputs):
        self.contents = list()
        
        for input in inputs:
            for _ in range(inputs[input]):
                self.contents.append(input)

    # Define a method for drawing a number of balls
    def draw(self, num):
        if len(self.contents) <= num:
            return self.contents
        
        items = list()

        for _ in range(0, num):    
            ball = self.contents.pop(int(random.random() * len(self.contents))) # Select a random ball from contents
            items.append(ball) # Add random ball to the list of drawn items
            # Finally, remove the ball from the list of drawn contents
            
        return items
        
# Design a function which uses an instance of the class to return a probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    last_count = 0 # Times that the expected ball is to be drawn

    for _ in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat) # Start each call with a new, separate hat instance
        expected_copy = copy.deepcopy(expected_balls) # make a copy of the expected balls arg
        list_of_drawn = copy_of_hat.draw(num_balls_drawn) # List of drawn balls

        for x in list_of_drawn: # Iterate through the array of drawn items
            if (x in expected_copy):
                expected_copy[x] -= 1 # Decrement index if the el is found
            
        if (all(val == 0 for val in expected_copy.values())):
            last_count += 1 # Increment the final count variable when the above condition is met

    fin = last_count / num_experiments

    return fin

hat1 = Hat(white=4, black=2, yellow=3)
hat2 = Hat(blue=2, green=5, red=4)
hat3 = Hat(orange=6, pink=2, purple=3, brown=5, striped=3)
print(hat3.draw(8))
exp = experiment(
    hat=hat3,
    expected_balls={'orange': 1, 'brown': 3},
    num_balls_drawn=5,
    num_experiments=1000
)

print(exp)