import re
def toID(str):
    return re.sub(r'[^a-z0-9]', '', str.lower())