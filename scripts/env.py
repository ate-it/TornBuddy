import os
from pathlib import Path

env_list = []


root_folder = Path(__file__).parents[1]
os.remove(root_folder / ".env.example")
with open(root_folder / ".env", "r") as fh_env:
    for env_line in fh_env:
        env_list.append(env_line.replace("\n", ""))

with open(root_folder / ".env.example", "a") as fh_env_example:
    for variable in env_list:
        if "#" not in variable and variable != "":
            var_only = variable.split("=")[0]
            fh_env_example.write(f"{var_only}=XXXXX\n")
        else:
            fh_env_example.write(f"{variable}\n")
