import argparse
import os

parser = argparse.ArgumentParser(description="Run a script in a subdirectory.")
subdirs = next(os.walk("./app"))[1]

dir_choices = {}
for sub in subdirs:
    dir_choices[sub] = {
        "main": f"--{sub}",
        "alias": f"-{sub[0:1]}",
        "dest": sub,
    }


for dir, cmd in dir_choices.items():
    parser.add_argument(
        cmd["main"],
        cmd["alias"],
        dest=cmd["dest"],
        action="store_true",
        help=f"Run script in '{dir}' directory.",
    )


args = parser.parse_args()

directory = None
for dir, cmd in dir_choices.items():
    if getattr(args, dir, False):
        if directory:
            exit(0)
        directory = dir

if __name__ == "__main__":
    if directory:
        script_path = os.path.join(os.getcwd(), "app", directory, "app.py")
        if os.path.exists(script_path):
            exec(open(script_path).read())
        else:
            print("Error: script not found")
