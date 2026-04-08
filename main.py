def main():
    print("Hello from is3-clase-versionado-26!")
    env = setup()
    print(f"Trabajando en entorno: {env}")

def setup():
    env = 'dev'
    return env


if __name__ == "__main__":
    main()
