import copy # a module containing methods related to copying different lists, objects, arrays, etc.
import random # a module which is composed of methods for generating random nums in various ways

class Hat:
    # 1. Instantiate an instance variable for the contents of the hat along with a dictionary for user inputs
    def __init__(self, **inputs):
        self.contents = []
        for n, m in inputs.items():
            for p in range(m):
                self.contents.append(n)

    # 2. Define a method for drawing a number of balls
    def draw(self, num):
        if len(self.contents) >= num:
            drawn_items = []

            for x in range(num):
                ball = random.choice(self.contents) # 3. Select a random ball from contents
                drawn_items.append(ball) # 4. Add random ball to the list of drawn items
                self.contents.remove(ball) # 5. Finally, remove the ball from the list of drawn contents
            return drawn_items
        else:
            return self.contents

# 6. Design a function which uses an instance of the class to return a probability
def experiment(hat, expected, num_drawn, num_of_experiments):
    drawn = 0 # 7. Times that the expected ball is to be drawn

    for x in range(num_of_experiments):
        copy_of_hat = copy.deepcopy(hat) # 8. Start each call with a new, separate hat instance
        list_of_drawn = copy_of_hat.draw(num_drawn) # 9. List of drawn balls
        corr = True # 10. Boolean val to check the correlation of list of drawn balls 
        
        for n, m in expected.items():
            # 11. Iterate through the key-val pairs to check whether not the corr bool is true
            if list_of_drawn.count(n) < m:
                corr = False
                break
        if corr:
            drawn += 1

    return drawn / num_of_experiments