from src import operations

#def say_hello():
  #  print("Hola Mundo!")

def calculate(a,b,operator):
    if operator == "+":
        return operations.add(a,b)
    elif operator == "-":
        return operations.substract(a,b)
    elif operator == "*":
        return operations.multiply(a,b)
    if operator == "/":
        return operations.divide(a,b)
    else:
        raise ValueError(f"Operador no valido{operator}")