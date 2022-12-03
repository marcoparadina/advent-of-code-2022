# Store the strategy guide in a dictionary
strategy_guide = {
    "A": "Y",
    "B": "X",
    "C": "Z"
}

# Define a dictionary to map each shape to its corresponding score
shape_score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Define a function to calculate the outcome of a round
def calculate_outcome(opponent_shape, your_shape):
    if opponent_shape == your_shape:
        # If the shapes are the same, it's a draw
        return 3
    elif (opponent_shape == "A" and your_shape == "Y") or (opponent_shape == "B" and your_shape == "Z") or (opponent_shape == "C" and your_shape == "X"):
        # If the opponent chose rock and you chose paper, or the opponent chose paper and you chose scissors, or the opponent chose scissors and you chose rock, you win
        return 6
    else:
        # Otherwise, you lose
        return 0

# Define a function to calculate the total score
def calculate_total_score(strategy_guide):
    total_score = 0
    for opponent_shape, your_shape in strategy_guide.items():
        # For each round, calculate the score for the shape and the outcome and add it to the total score
        total_score += shape_score[your_shape] + calculate_outcome(opponent_shape, your_shape)
    return total_score

# Print the total score
print(calculate_total_score(strategy_guide))


