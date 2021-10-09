#!/usr/bin/python3

import sys

args = sys.argv[1:]

with open("installed.txt", "r") as f:
    preinstalled = f.read().split("\n")

with open("skipped.txt", "w") as f:
    f.write("")

def ad2(arg, filename):
    with open(filename, "a") as f:
        f.write(arg + "\n")

args = list(filter(lambda x: x not in preinstalled, args))

if len(args) == 0:
    print("All arguments are already installed. Exiting now.")
    exit(0)

skipped = 0
for arg in args:

    while True:
        print(f"Please install {arg}")
        x = input("Done? yes/y or skip/s/no/n\n\t")
        
        if x in ["yes", "y"]:
            ad2(arg, "installed.txt")
            print(f"Installed {arg}")
            break

        if x in ["skip", "s", "no", "n"]:
            ad2(arg, "skipped.txt")
            print(f"Skipped {arg}")
            skipped += 1
            break

        print(f"Your input, `{x}`, isn't valid.")
    
def re2(filename):
    with open(filename, "r") as f:
        x = f.read()
        x = x.split("\n")
        x = ["\t"+xs for xs in x]
        x = "\n".join(x)
        return x


print("These arguments were installed (now or from the cache)):")
print(re2("installed.txt"))

if skipped == 0:
    print("All arguments are installed. Exiting now.")
    exit(0)

print("These arguments were skipped:")
print(re2("skipped.txt"))
