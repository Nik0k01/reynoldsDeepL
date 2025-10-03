# Import necessary library to run multiple processes at the same time
from concurrent.futures import ProcessPoolExecutor, as_completed
import os
from PyFoam.Execution.BasicRunner import BasicRunner
import re

# Pattern to match numbers with exactly 2 decimal places
pattern = r'\d+\.\d{2}'
# Directory containing the flow cases
case_directory = "flowCases/"
case_list = os.listdir(case_directory)

def solve_flow(case_name):
    # Wrapper for BasicRunner - solving the case
    # Path to openFoam's simpleFoam solveer
    solver = "simpleFoam"
    runner = BasicRunner(argv=[solver, "-case", case_name],
                        silent=True,
                        server=False,
                        logname="solverLog")
    runner.start()
    # Get the Reynolds value
    match = re.search(pattern, case_name)
    if match:
        Re = match.group(0)  
    else:
        raise ValueError("No Reynolds number found in the case name.")
    return Re, case_name, runner.runOK(), "done"

# Running multiple cases at once to save time
with ProcessPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(solve_flow, case_name = os.path.join(case_directory, case)) for case in case_list]
    for f in as_completed(futures):
        Re, case_name, ok, msg = f.result()
        print(f"{case_name} [Re={Re}] -> {msg}, success={ok}")
