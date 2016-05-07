import random

def main():
    d = {'table': 'under the table', 'server': 'tangled in the wires'}

    key = random.choice(d.keys())
    print(d(key))

main()