# Text to append
text_to_append = "This is the appended text."

# Open the file in append mode and write the new text
with open(r"C:\\Users\\ASUS\\Desktop\\text1.txt", "a") as file2:
    file2.write(text_to_append + "\n")

# Open the file in read mode and display the content
with open(r"C:\\Users\\ASUS\\Desktop\\text1.txt", "r") as file2:
    content = file2.read()
    print("Updated file content:\n")
    print(content)

