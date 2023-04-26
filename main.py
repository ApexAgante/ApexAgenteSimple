import argparse
import os

parser = argparse.ArgumentParser(description='Run a script in a subdirectory.')
subdirs = next(os.walk('.'))[1]
choices = {f"--{d}": d for d in subdirs}
for i, value in choices.items():
    parser.add_argument(i, action='store_true')

args = parser.parse_args()

directory = None
for choice, value in choices.items():
    if getattr(args, value, False):
        if directory:
            print("Error: too many directories specified.")
            exit(1)
        directory = value
        
if directory:
    script_path = os.path.join(os.getcwd(), directory, 'app.py')
    if os.path.exists(script_path):
        exec(open(script_path).read())
    else:
        print(f"Error: script {args.script} not found")




