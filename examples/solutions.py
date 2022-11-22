def card_constraint1():
    print("""
# Constraints: Each card in exactly one position
for c in CARDS:
    prob += lpSum(choices[c][p] for p in POSITIONS) == 1
""")

def card_constraint2():
    print("""
# Constraints: Each position has exactly one card
for p in POSITIONS:
    prob += lpSum(choices[c][p] for c in CARDS) == 1
""")

def card_objective():
    print("""
# add objective
prob += lpSum(obj_coeffs[c][p]*choices[c][p] for c in CARDS for p in POSITIONS)
""")

def roster_variables():
    print("""
y = LpVariable.dicts(
    name="y",
    indices=W,
    cat="Binary",
)

x = LpVariable.dicts(
    name="x",
    indices=(W, S),
    cat="Binary",
)
""")

def roster_objective():
    print("""
prob += (
    lpSum(y[w] for w in W),
    "Number of hired workers"
)
""")

def roster_constraint1():
    print("""
for s in S:
    prob += (
        lpSum(x[w][s] for w in W) == 1,
        f"Shift {s} covered",
    )
""")

def roster_constraint2(hint=False):
    if hint:
        print("""
for s in S:
    for w in W:
        prob += (
            ...,
            f"Shift {s}, worker {w} covered by hired worker",
        )
""")
    else:
        print("""
for s in S:
    for w in W:
        prob += (
            x[w][s] <= y[w],
            f"Shift {s}, worker {w} covered by hired worker",
        )
""")


def roster_constraint3(hint=False):
    if hint:
        print("""
for s1, s2 in shift_conflicts:
    for w in W:
        prob += (
            ...,
            f"Shift {s1}, shift {s2} conflict for worker {w}",
        )
""")
    else:
        print("""
for s1, s2 in shift_conflicts:
    for w in W:
        prob += (
            x[w][s1] + x[w][s2] <= 1,
            f"Shift {s1}, shift {s2} conflict for worker {w}",
        )
""")