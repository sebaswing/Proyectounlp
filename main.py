from src import calculator

def main():
    #calculator.say_hello()
    print("welcome to the calculator!")
    num1= float(input("escriba el primer numero"))
    print("enter second number")
    num2= float(input())
    operator=input("digité el operador (+,-,*,/)")
    result = calculator.calculate (num1,num2,operator)
    print(f"the result is : {result}")

if __name__== "__main__": #la idea acá es unicamente ejecutar el main cuando se llame directamente no en la consola interactiva
    main()