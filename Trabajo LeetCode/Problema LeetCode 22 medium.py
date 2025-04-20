#22. Generate Parentheses
#Medium
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# dados n pares de paréntesis, escribe una función para generar todas las combinaciones de paréntesis bien formados.

n=input("Introduce el número de pares de paréntesis: ")
if n.isdigit():
    n=int(n)
else:
    print("El valor introducido no es un número entero.")

resultado_parentesis= "(" *n + ")"*n

print("El resultado es: ", resultado_parentesis)