# Run this script to run the python files located in the src folder
# In terminal, run the following command: python main.py
import os

# Get the current working directory
cwd = os.getcwd()

# Get the path of the src folder
src_folder = os.path.join(cwd, 'src')

# Get the list of files in the src folder
files = os.listdir(src_folder)

# Run the python files in the src folder
for file in files:
    if file.endswith('.py'):
        file_path = os.path.join(src_folder, file)
        os.system(f'python {file_path}')
        print(f'Finished running {file}\n')