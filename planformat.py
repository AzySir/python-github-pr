from gzip import READ
from pickle import REDUCE


RED    = '\033[41m'
YELLOW  = '\033[93m'
GREEN   = '\033[42m'
END = '\033[0m'

def add(line):
    return GREEN + line + END

def edit(line):
    return YELLOW + line + END

def destroy(line):
    return RED + line + END