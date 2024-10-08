# The following function wil be used to keep track of the opponent's history and plays whatever the opponent played two plays ago..

fin = {}

def player(prev_play, opponent_history=[]):
    global fin

    i = 5

    if prev_play in ["R", "P", "S"]:

        opponent_history.append(prev_play)

    guess = "R" # The default until the logic begins to run

    if len(opponent_history) > i:
        input = "".join(opponent_history[-i:])
        
        if "".join(opponent_history[-(i+1):]) in fin.keys():
            fin["".join(opponent_history[-(i+1):])] += 1
        else:
            fin["".join(opponent_history[-(i+1):])] = 1

        output = [input+"R", input+"P", input+"S"]

        for n in output:
            if not n in fin.keys():
                fin[n] = 0

        est = max(output, key = lambda key: fin[key])

        if est[-1] == "P":
            guess = "S"
        if est[-1] == "R":
            guess = "P"
        if est[-1] == "S":
            guess = "R"

    return guess
