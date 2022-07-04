import sys
import logging
from github import *
from planformat import *
# 1) Configuration
FILENAME = "plan_pr.json"
logging.basicConfig()
log = logging.getLogger("app")
log.setLevel(logging.DEBUG)

IN_ADD = False
IN_EDIT = False
IN_DESTROY = False
IN_EDIT_CONTAINER = False

# a) Set File Name
def readlines(path):
    lines = open(path, "r+")
    line = lines.readlines()   
    return line

# b) Read Lines

# c) GITHUB API - Read from Environment Variables

def reset_globals():
    global IN_ADD, IN_EDIT, IN_DESTROY
    IN_ADD = False
    IN_EDIT = False
    IN_DESTROY = False

def check_end(line):
    global IN_ADD, IN_EDIT, IN_DESTROY, IN_EDIT_CONTAINER
    if line.strip().replace("\n", "").startswith("}"):
        if IN_ADD is True:
            line = add(line)
        elif IN_EDIT is True:
            line = edit(line)
        elif IN_DESTROY is True:
            line = destroy(line)
        elif IN_EDIT_CONTAINER is True:
            line = edit(line)
            IN_EDIT_CONTAINER = False
        reset_globals()
        return True, line
    else:
        return False, line

# d) formatting
def check(line):
    global IN_ADD, IN_EDIT, IN_DESTROY, IN_EDIT_CONTAINER
    end, line = check_end(line)
    if not end:
        if line.replace("\n", "").lstrip().startswith("-"): # If starts with - (destroy)
            IN_DESTROY = True
            line = destroy(line)
        elif line.replace("\n", "").lstrip().startswith("+"): # If starts with + (add)
            IN_ADD = True
            line = add(line)
        elif line.replace("\n", "").lstrip().startswith("~") and "resource" in line:
            IN_EDIT_CONTAINER = True
            line = edit(line)
        elif line.replace("\n", "").lstrip().startswith("~"): # If starts with ~ (edit)
            IN_EDIT = True
            line = edit(line)
        return line
    else:
        return line

def run():
    if len(sys.argv) <= 1:
        raise Exception('You have not provided a path/filename for the plan.json') 
    else:
        if sys.argv[1].endswith(".json"):
            lines = readlines(sys.argv[1])
            for x in lines:
                log.debug(check(x).replace("\n", ""))
        else:
            raise Exception('The state must be in a json format') 
        

if __name__ == "__main__":
    run()