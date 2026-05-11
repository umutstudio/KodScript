def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "oyun":
            ast.append({"type": "game", "value": tokens[i+2]})
            i += 3
        else:
            i += 1
    return ast
