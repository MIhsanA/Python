file = open("ihsan.txt", "r")
print(file.readline(2))


Example_file = open("Example_file.txt", "r")

outfile = ""

for line in range(10):
    if line % 2 == 0:
        outfile += Example_file.readline()
    else:
        Example_file.readline()
Example_file.close
Example_file = open("Example_file.txt", "w")
Example_file.write(outfile)
Example_file.close()