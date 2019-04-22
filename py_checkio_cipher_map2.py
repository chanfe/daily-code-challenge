# "Nikola, A1213pokl, bAse730onE."
#
# "Yes Sofia, what is it?"
#
# "You tell me! Your torture device is singing my circuits with its new lexicon. There is no way I can remember these new passwords and the thing doesn't accept simple and easy ones!"
#
# "Oh, those will be good passwords, you can use them."
#
# "Why can’t you use them!?" Sofia asked almost hysterically. "I’ve already forgotten them! Do you want me locked out of my own house for eternity? Come up with something easier so I don’t have to keep all that randomized gobbledygook in my head." Sofia rarely acted so demanding but she had reached her boiling point. The stress of the past few days coupled with her exhaustion had brought her to the edge.
#
# "Don’t worry, I was expecting something easier to remember. Why don’t you use the cipher map to help with your password. With it we can encrypt all the passwords and leave them right next to the door or in a special place that we all agree upon. You will only be able to read them with the use of the cipher map which we will take with us on our trip.
#
# "So I don’t need to remember all of those passwords? All we have to do is make sure that we don't lose the cipher map." asked Sofia with hopefully.
#
# "Yes, that is correct."
#
# "Awesome. Show me the cipher map and explain how this works one more time."
#
# Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher map. A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down the final four symbols of the password. Without the same cipher grille, it is difficult to discern the password from the resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.
#
#
#
# Write a module that enables the robots to easily recall their passwords through codes when they return home.
#
# The cipher grille and the ciphered password are represented as an array (tuple) of strings.
#
# Input: A cipher grille and a ciphered password as a tuples of strings.
#
# Output: The password as a string.
#
# Example:
#
# recall_password(
#     ('X...',
#      '..X.',
#      'X..X',
#      '....'),
#     ('itdf',
#      'gdce',
#      'aton',
#      'qrdi')) == 'icantforgetiddqd'
#
# recall_password(
#     ('....',
#      'X..X',
#      '.X..',
#      '...X'),
#     ('xhwc',
#      'rsqx',
#      'xqzz',
#      'fyzr')) == 'rxqrwsfzxqxzhczy'
#
# How it is used: Here you can learn how to work with 2D arrays. You also get to learn about the ancient Grille Cipher, a technique of encoding messages which has been used for half a millenium. The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.
#
# Precondition: len(cipher_grille) == 4
# len(ciphered_password) == 4
# all(len(row) == 4 for row in ciphered_password)
# all(len(row) == 4 for row in cipher_grille)
# all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
# all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

def recall_password(cipher_grille, ciphered_password):
    temp_cipher = cipher_grille
    answer = ""
    answer += str(decrypt(cipher_grille, ciphered_password))
    for i in range(3):
        temp_cipher = rotate(temp_cipher)
        answer += decrypt(temp_cipher, ciphered_password)
    print(answer)
    return answer

def decrypt(cipher_grille, ciphered_password):
    part_answer = ""
    count_i = 0
    for i in cipher_grille:
        count_j = 0
        for j in i:
            if j == "X":
                part_answer += ciphered_password[count_i][count_j]
            count_j += 1
        count_i += 1
    return part_answer

def rotate(cipher_grille):
    new_tuple = ()
    p = ''
    for i in range(4):
        for j in reversed(cipher_grille):
            p += j[i]
        new_tuple = new_tuple + (p,)
        p = ''
    return new_tuple

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
