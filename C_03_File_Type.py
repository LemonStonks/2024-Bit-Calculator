# ask users for file type (integer/ image / text / xxx)
def get_file_type():


    while True:
        response = input("File type: ").lower()
        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int',]:
            return "integer"

        # check for an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is invalid output an error and continue the loop
        else:
            print("Please enter a valid file")




# Main routine goes here
while True:
    file_type = get_file_type()

    # if user choice 'i', ask if they want an image / integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "i":
            file_type = "integer"
        else:
            file_type = "image"
            break

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break

while True:
    file_type = get_file_type()

    # if user choice 'i', ask if they want an image / integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "i":
            file_type = "integer"
        else:
            file_type = "image"
            break

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break

print()
print("Thank you for using the file type selection")






