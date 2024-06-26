import sys

arguments = sys.argv[1:]  # Exclude the first argument which is the script name

print("Arguments:")
for arg in arguments:
    print(arg)

print(f"Number of arguments is {len(arguments)}")
