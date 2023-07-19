def main():
    while True:
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


def encode(password):
    encoded_password = ""
    for digit in password:
        # Shifting each digit up by 3 numbers
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password




if __name__ == "__main__":
    main()
