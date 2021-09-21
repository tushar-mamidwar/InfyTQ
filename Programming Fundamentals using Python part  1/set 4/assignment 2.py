"""
Problem Statement
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note:

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

    Sample Input                                Expected Output

the sun rises in the east               eht snu sesir ni eht stea


"""
#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    sentence = sentence.split(" ")
    encrypted_sentence=""
    counter=1
    for word in sentence:
        vowels_in_word = ""
        consonant_in_word = ""
        if counter%2==0:
            for character in word:
                if character not in vowels:
                    consonant_in_word+=character
                else:
                    vowels_in_word+=character

            encrypted_sentence+= consonant_in_word+vowels_in_word+" "
        else:
            encrypted_sentence+= word[::-1]+' '
        counter+=1
    encrypted_sentence=encrypted_sentence[:-1]
    return encrypted_sentence




sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)