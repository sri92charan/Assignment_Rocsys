# Assignment_Rocsys
Repository for rocsys endurance tester. Use the following instructions to run the developed python code

Prerequisites for running the python code:
- appropriate version of Python 
- python path added to Env variables
- git command line utility for Linux
- git path added to env variable

Steps to run the code
- open the terminal on the linux system where you intend to run the code
- change directory to where you want to install using "cd /path/to/dir"
- verify the path using the command "pwd"
- clone the git repo using the command "git clone https://github.com/sri92charan/Assignment_Rocsys.git"
- get into the python file directory by using the cmd "cd Assignment_Rocsys"
- run the file using "python enduranceTestROC1"

- The code runs and creates a logfile in the same directory

- **Future improvements**
- Will create a logfile preferably in the csv format (cycle number, Step name, Moment of step happening, Result)
- CSV format makes it easy for other applications to parse and use the data
- Will also generate a graph at the end of the test to show the number/ percentage of failure (visual representation is always better)
