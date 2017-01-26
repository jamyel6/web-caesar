
def rotate_character(char, rot):
    cipherText = ""
    for ch in char:
        if ch.isalpha():
            if ch.isupper():
                rot_ascii_number = (((ord(ch) % 65) + rot)%26)+65
                finalLetter = chr(rot_ascii_number)
            else:
                rot_ascii_number = (((ord(ch) % 97) + rot)%26)+97
                finalLetter = chr(rot_ascii_number)
            cipherText += finalLetter
        else:
            cipherText += ch

    return cipherText
