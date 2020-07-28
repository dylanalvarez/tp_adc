import sympy as sym

s, t = sym.symbols('s, t')
expression = (
        4 /
        (20 * s ** 2 + 2 * s + 5)
)

print(sym.inverse_laplace_transform(expression, s, t))
