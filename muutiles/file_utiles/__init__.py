import os
def read(filename):
    if os.path.exists(filename):
        with open(filename,'r') as f:
            return f.read()
    else:
        return None

def write(filename,content):
    with open(filename,'w') as f:
        f.write(content)