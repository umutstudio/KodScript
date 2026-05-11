def generate(ast):
    code = []
    for node in ast:
        if node["type"] == "game":
            code.append(f"create_game('{node['value']}')")
        elif node["type"] == "app":
            code.append(f"create
