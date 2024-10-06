try:
    # Open the file in read mode
    with open(r"C:\\Users\\ASUS\\Desktop\\text1.txt", "r") as file2:
        # Read the content of the file
        content = file2.read()
    
    # Print the content
    print(content)
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")