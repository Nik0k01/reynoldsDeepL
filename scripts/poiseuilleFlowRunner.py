# Import necessary library to run multiple processes at the same time
from concurrent.futures import ProcessPoolExecutor, as_completed
import os
from PyFoam.Execution.BasicRunner import BasicRunner

case_directory = "poiseuilleFlowCases/"
case_list = os.listdir(case_directory)

def run_poiseuille_flow(case_name):
    # Wrapper for BasicRunner - solving the case
    # Path to openFoam's simpleFoam solveer
    solver = "simpleFoam"
    runner = BasicRunner(argv=[solver, "-case", case_name],
                        silent=True,
                        server=False,
                        logname="solverLog")
    runner.start()
    # Get the Reynolds value
    Re = case_name.split("-")[-1]
    return Re, runner.runOK(), "done"

# Running multiple cases at once to save time
with ProcessPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(run_poiseuille_flow, case_name = os.path.join(case_directory, case)) for case in case_list]
    for f in as_completed(futures):
        Re, ok, msg = f.result()
        print(f"[Re={Re}] -> {msg}, success={ok}")
