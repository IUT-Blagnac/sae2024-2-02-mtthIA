def rle_encode(input_string):
    if not input_string:
        return ""

    encoded_string = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_string.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_string.append(f"{count}{current_char}")
    return ''.join(encoded_string)
