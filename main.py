from .lexer import tokenize
from .parser import parse
from .codegen import generate
from .runtime import run

from compiler import tokenize, parse, generate, run

with open("examples/simple_game.yeni", "r", encoding="utf-8") as f:
    code = f.read()

tokens = tokenize(code)
ast = parse(tokens)
generated_code = generate(ast)
run(generated_code)
