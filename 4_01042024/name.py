import sys
def run (name:str):
    print(f"Hi {name}!")

if __name__ == "__main__":
    name = sys.argv[1]

    run(name=name)