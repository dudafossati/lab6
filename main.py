def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password format. Please enter an 8-digit password containing only integers.")
            else:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
        elif choice == '2':
            decoded_password = decode(encoded_password)
            print("The encoded password is", encoded_password, "and the original password is", decoded_password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def decode(string):
    new = ""
    for num in string:
        if (int(num) - 3) >= 0:  ## checks if the current num in encode string when subtracted 3 is greater than or equal to 0
            new = new + str((int(num) - 3))
        elif (int(num) - 3) == -3:
            new = new + str(7)
        elif (int(num) - 3) == -2:
            new = new + str(8)
        elif (int(num) - 3) == -1:
            new = new + str(9)
    return new

def encode(password):
    encoded_password = ""
    for digit in password:
        # Shifting each digit up by 3 numbers
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password




if __name__ == "__main__":
    main()
