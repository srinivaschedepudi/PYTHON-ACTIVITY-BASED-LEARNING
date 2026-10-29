"""Case 35: Text compression using consecutive character runs."""

SAMPLES = ["aaabbcccc", "abcd"]


def encode_runs(text):
    if text == "":
        return ""
    encoded = ""
    current_character = text[0]
    count = 1
    for index in range(1, len(text)):
        if text[index] == current_character:
            count += 1
        else:
            encoded += current_character
            if count > 1:
                encoded += str(count)
            current_character = text[index]
            count = 1
    encoded += current_character
    if count > 1:
        encoded += str(count)
    return encoded


def compress_if_beneficial(text):
    encoded = encode_runs(text)
    if len(encoded) < len(text):
        return encoded, True
    return text, False


def main():
    print("RUN-LENGTH COMPRESSION")
    for text in SAMPLES:
        result, saved_space = compress_if_beneficial(text)
        print(f"Input: {text}")
        print(f"Encoded candidate: {encode_runs(text)}")
        print(f"Stored result: {result}")
        print(f"Compression beneficial: {saved_space}")


if __name__ == "__main__":
    main()
