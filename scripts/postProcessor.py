"""To run this script you must have openFOAM sourced in your terminal"""
import subprocess
import os 

case_directory = "flowCases/"
cases = os.listdir(case_directory)
case_list = [os.path.join(case_directory, a_case) for a_case in cases]

# Create the post process dict for each case
for case_dir in case_list:
    print(f"Post processing {case_dir}")
    subprocess.run(["postProcess", "-case", case_dir, "-func", "'patchAverage(name=inlet,p)'"])
    