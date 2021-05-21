NOTES = ["Marcos 10\n", "Felipe 4\n", "José 6\n", "Ana 10\n", "Maria 9\n", "Miguel 5"]

write_file = open("notes.txt", mode="w")
write_file.writelines(NOTES)
write_file.close()

file = open("notes.txt", "r")
lines = file.readlines()
file.close()

new_file = open("notes.txt", "w")
for line in lines:
    if (int(line.strip("\n").split()[1]) > 5):
        new_file.write(line)
new_file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()


