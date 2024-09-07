class Category:
    def __init__(self, title): # the __init__ fn here houses the title instance variable as a parameter 
        self.title = title # the name of the category 
        self.ledger = [] # ledger which all the financial details and amounts

    def get_balance(self): # class method which is responsible for recording the present balance
        balance = 0 # int obj for storing the current balance
        for x in self.ledger:
            balance += x['amount'] # iteation to keep the balance updated accordingly (that is, for each function call that alters the ledger)
        return balance # current balance is always returned

    def check_funds(self, amount): # fn which takes amount as a parameter, and returns a boolean based on the get_balance method
        return amount <= self.get_balance()

    def deposit(self, amount, description=""): # class method used for depositing money
        self.ledger.append({'amount': amount, "description": description})        
        # return self.ledger # commented out in order to avoid conflict with final return
    
    def withdraw(self, amount, description=""): # class method used for withdrawing money
        if self.check_funds(amount): 
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        
        return False
    
    def transfer(self, amount, instance): # method which transfers money between different budget categories
        if self.withdraw(amount, 'Transfer to ' + instance.title): # conditional which verifies if withdraw was called on class obj
            instance.deposit(amount, 'Transfer from ' + self.title)
            return True

        return False
    
    def __str__(self): # fn of class which will be responsible for generating the final string output 
        fin = "" # str obj which will store the final output of the method and class
        fin += self.title.center(30, "*") + "\n"

        total = 0
        for x in self.ledger:
            total += x['amount']
            
            fin += x['description'].ljust(23, " ")[:23]
            fin += "{0:>7.2f}".format(x['amount'])
            fin += "\n"
        
        fin += 'Total: ' + "{0:.2f}".format(total)
        return fin
  
# function outside of method which is responsible for creating a spend chart for each category
def gen_spend_chart(categories):
    fin = "Percentage Spent By Category\n"

    # Below are a series of lists which retrieve total expenses of each category
    total = 0
    titles = []
    expenses = []
    len_titles = 0

    for i in categories:
        expense = sum([-x['amount'] for x in i.ledger if x['amount'] < 0])
        total += expense

        if len(i.title) > len_titles:
            len_titles = len(i.title)
        
        expenses.append(expense)
        titles.append(i.title)

    expenses = [(x / total) * 100 for x in expenses]
    titles = [title.ljust(len_titles, " ") for title in titles]

    for y in range(100, -1 , -10):
        fin += str(y).rjust(3, " ") + "|"
        for x in expenses:
            fin += " o " if x >= y else "   "
        fin += " \n"
    
    fin += "    " + "---" * len(titles) + "-\n"

    for n in range(len_titles):
        fin += "    "
        for title in titles:
            fin += f' {title[n]} '
        fin += " \n"

    return fin.strip("\n")
