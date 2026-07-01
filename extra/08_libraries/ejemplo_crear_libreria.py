import os

os.system("cls")  # Limpiar la consola (en Windows)


def main():
    hello("World")
    goodbye("World")
    
def hello(name):
    print(f"Hello, {name}!")
    
def goodbye(name):
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    main()