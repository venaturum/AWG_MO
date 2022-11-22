card_constraint1 = """
# Constraints: Each card in exactly one position
for c in CARDS:
    prob += lpSum(choices[c][p] for p in POSITIONS) == 1
"""

card_constraint2 = """
# Constraints: Each position has exactly one card
for p in POSITIONS:
    prob += lpSum(choices[c][p] for c in CARDS) == 1
"""