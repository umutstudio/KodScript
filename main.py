from compiler.lexer import tokenize
from compiler.parser import parse
from compiler.codegen import generate
from compiler.runtime import run

with open("examples/simple_game.yeni", "r", encoding="utf-8") as f:
    code = f.read()

tokens = tokenize(code)
ast = parse(tokens)
generated_code = generate(ast)
run(generated_code)
