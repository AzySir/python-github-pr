def add(line):
    return '\x1b[5;37;42m' + line + '\x1b[0m'

def edit(line):
    return '\x1b[3;37;43m' + line + '\x1b[0m'

def destroy(line):
    return '\x1b[5;37;41m' + line + '\x1b[0m'