    # Step 1: Take user input and write to file
user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as w:
    w.write(user_input + "\n")

# Step 2: Take additional input and append to file
additional_input = input("Enter additional text to append: ")

with open("output.txt", "a") as a:
    a.write(additional_input + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as r:
    content = r.read()
    print(content)
