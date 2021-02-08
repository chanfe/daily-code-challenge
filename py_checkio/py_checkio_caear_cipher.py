# This mission is the part of the set. Another one - Caesar cipher decriptor.
#
# Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
#
# example
#
# Input: A secret message as a string (lowercase letters only and white spaces)
#
# Output: The same string, but encrypted
#
# Example:
#
# to_encrypt("a b c", 3) == "d e f"
# to_encrypt("a b c", -3) == "x y z"
# to_encrypt("simple text", 16) == "iycfbu junj"
# to_encrypt("important text", 10) == "swzybdkxd dohd"
# to_encrypt("state secret", -13) == "fgngr frperg"
#
# How it is used: For cryptography and to save important information.
#
# Precondition:
# 0 < len(text) < 50
# -26 < delta < 26

def to_encrypt(text, delta):
    #replace this for solution
    text_array = text.split(" ")
    answer = []
    for i in range(len(text_array)):
        temp_text_var = ""
        for j in text_array[i]:
            ascii_number = ord(j) + delta
            if ascii_number < 97:
                ascii_number += 26
            elif ascii_number > 122:
                ascii_number -= 26
            temp_text_var += chr(ascii_number)
        answer.append(temp_text_var)
    return " ".join(answer)

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
