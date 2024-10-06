def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        # Get the last n lines
        last_n_lines = lines[-n:]
        return last_n_lines

# Specify the file path and number of lines to read
file_path = r"C:\\Users\\ASUS\\Desktop\\text1.txt"
n = 1

# Read and print the last n lines
last_lines = read_last_n_lines(file_path, n)
print("Last {} lines of the file:".format(n))
for line in last_lines:
    print(line, end='')

