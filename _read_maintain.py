lines = open('maintain.py').readlines()
for i in range(204, 295):
    print(f"{i+1}: {lines[i].rstrip()}")
