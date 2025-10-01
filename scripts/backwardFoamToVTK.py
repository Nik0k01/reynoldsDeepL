import subprocess
import os 

case_directory = "backwardStepCases/"
cases = os.listdir(case_directory)
case_list = [os.path.join(case_directory, a_case) for a_case in cases]

for case_dir in case_list:
    print(f"Converting {case_dir} to VTK...")
    subprocess.run(["foamToVTK", "-case", case_dir])
    