file = open("notes.txt", "w")
file.write("english homework\n")
file.write("Math Homework\n")
file.write("Social Studies Homework\n")
file.write("Science Project\n")
file.write("Math Chart\n")
file.close()


file = open("notes.txt", "r")
print("show first 20 characters:")
print(file.read(20))
file.close()

print()


file = open("notes.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

print()


print("Readline by line:")
file = open("notes.txt", "r")
for line in file:
    print(line.strip())
file.close()

print()


file = open("notes.txt", "r")
newfile = open("pythonnotes.txt", "w")

print("Filtered Notes:")

for line in file:
    if "Python" in line:
        print(line.strip())
        newfile.write(line)

file.close()
newfile.close()

print("\nFiltered notes have been copied to 'pythonnotes.txt'.")