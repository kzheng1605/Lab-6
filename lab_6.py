# Kevin Zheng
def encode(string):
    char_list = []
    encode_string = ""
    # Converts the string into a list
    for index in range(len(string)):
        char_list.append(int(string[index]))
    # Encodes the elements of the list
    for index in range(len(char_list)):
        char_list[index] = (char_list[index] + 3) % 10
    # Makes the new string
    for index in range(len(char_list)):
        encode_string = encode_string + str(char_list[index])

    return encode_string


def print_options():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def main():
    print_options()

    user_input = int(input("Please enter an option: "))
    num = 0
    encode_num = 0

    while user_input != 3:
        if user_input == 1:
            num = input("Please enter your password to encode: ")
            encode_num = encode(num)
            print("Your password has been encoded and stored!")

        if user_input == 2:

            print(f"The encoded password is {encode_num},", end=" ")
            print(f"and the original password is {num}.")

        print_options()

        user_input = int(input("Please enter an option: "))


if __name__ == "__main__":
    main()
