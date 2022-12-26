import os

files_to_process = [
    r'./math_sin_square.py',
    r'./math_square_root.py',
]
for path in files_to_process:
    with open(path) as source:
        print(os.path.basename(path).center(200, '-'))
        exec(source.read())
