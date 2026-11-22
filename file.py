# Writing data into a file
file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Course: B.Tech CSE\n")
file.write("College: GGI\n")

file.close()

# Reading data from the file
file = open("student.txt", "r")

data = file.read()
print(data)

file.close()