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
    print("\n0. Exit")
    print("1. Encode")
    print("2. Decode\n")


def main():
    print_options()

    user_input = int(input("Select from the following options: "))
    num = 0

    while user_input != 0:
        if user_input == 1:
            num = input("Enter a number to be encoded: ")
            encode_num = encode(num)
            print(encode_num)

        if user_input == 2:
            num = input("Enter a number to be decoded: ")
            # decode_num = decode(num)
            # print(decode_num)

        print_options()

        user_input = int(input("Select from the following options: "))


if __name__ == "__main__":
    main()
