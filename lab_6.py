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


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
