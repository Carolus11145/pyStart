import copy # a module containing methods related to copying different lists, objects, arrays, etc.
import random # a module which is composed of methods for generating random nums in various ways

class Hat:
    # 1. Instantiate an instance variable for the contents of the hat along with a dictionary for user inputs
    def __init__(self, **inputs):
        self.contents = list()
        
        for input in inputs:
            for i in range(inputs[input]):
                self.contents.append(input)

    # 2. Define a method for drawing a number of balls
    def draw(self, num):
        if len(self.contents) < num:
            return self.contents
        
        elif len(self.contents) >= num:
            items = list()

            for x in range(0, num):
            
                ball = random.choice(self.contents) # 3. Select a random ball from contents
                items.append(ball) # 4. Add random ball to the list of drawn items
                self.contents.remove(ball) # 5. Finally, remove the ball from the list of drawn contents
            
            return items
        
# 6. Design a function which uses an instance of the class to return a probability
def experiment(hat, expected, num_drawn, num_of_experiments):
    last_count = 0 # 7. Times that the expected ball is to be drawn

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
            last_count += 1

    fin = last_count / num_of_experiments

    return fin

hat1 = Hat(white=4, black=2, yellow=3)
print(hat1.draw(4))
print(hat1.draw(5))
exp = experiment(
    hat=hat1,
    expected={'red': 1, 'green': 2},
    num_drawn=5,
    num_of_experiments=100
)

print(exp)