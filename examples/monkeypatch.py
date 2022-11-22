from pulp import PULP_CBC_CMD, LpProblem

original_solve_method = LpProblem.solve

def solve(prob):
    solver = PULP_CBC_CMD(logPath=r'log.txt', msg=False)
    original_solve_method(prob, solver=solver)
    with open('log.txt', 'r') as f:
        print(f.read())

LpProblem.solve = solve