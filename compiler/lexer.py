import re

def tokenize(code):
    tokens = re.findall(r"[a-zA-Z_]+|\d+|:|;", code)
    return tokens
