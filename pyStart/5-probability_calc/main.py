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
            contents = copy.deepcopy(self.contents)
            self.contents.clear()
            return contents
        
        items = list()

        for _ in range(0, num):    
            ball = random.randint(0, len(self.contents) - 1) # Select a random ball from contents
            items.append(self.contents.pop(ball)) # Add random ball to the list of drawn items
            # Finally, remove the ball from the list of drawn contents
            
        return items
        
# Design a function which uses an instance of the class to return a probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    origin_hat = copy.copy(hat)
    last_count = 0 # Times that the expected ball is to be drawn

    for _ in range(num_experiments):
        copy_of_hat = copy.deepcopy(origin_hat) # Start each call with a new, separate hat instance
        list_of_drawn = copy_of_hat.draw(num_balls_drawn) # List of drawn balls
        corr = True # Boolean val to check the correlation of list of drawn balls 
        
        for n, m in expected_balls.items():
            # Iterate through the key-val pairs to check whether not the corr bool is true
            if list_of_drawn.count(n) < m:
                corr = False
                break
        
        if corr:
            last_count += 1
    # Final return value of the experiment function
    return last_count / num_experiments

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
