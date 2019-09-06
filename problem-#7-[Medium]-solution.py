def decode(message):
    if len(message) <= 1:  # this will be true at the very end of each recursive execution
        return 1  #

    if len(message) >= 2:
        if 1 <= int(''.join(message[0:2])) <= 26:  # check if joined 1st and 2nd element are in the valid range [1-26]
            return decode(message[1:]) + decode(message[2:])

        return decode(message[1:])  # call decode() recursively, removing the first element of the message


def main():
    encoded_message = list("111")  # convert to list to be able to work with each element

    print(decode(encoded_message))  # returns 3


if __name__ == "__main__":
    main()
