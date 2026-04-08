def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


def main():
    print("Hello from is3-clase-versionado-26!")
    env = setup()
    print(f"Trabajando en entorno: {env}")
    result = suma(5, 3)
    print(f"La suma de 5 y 3 es: {result}")


def setup():
    env = "dev"
    return env


if __name__ == "__main__":
    main()
