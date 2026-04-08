def suma(a, b):
    return a + b


def main():
    print("Hello from is3-clase-versionado-26!")
    env = setup()
    print(f"Trabajando en entorno: {env}")
    result = suma(5, 3)
    print(f"La suma de 5 y 3 es: {result}")


def setup():
    env = 'dev'
    return env


if __name__ == "__main__":
    main()
