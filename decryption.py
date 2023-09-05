cipher_text = input('what is the encrypted message?:')

shift_key = int(input('what is the key?:'))

normal_text = ''

# iteration over the given text
for letter in cipher_text:   
   # checking for a space
    if letter == ' ':
        normal_text += ' '    
    elif letter.isupper():
        # get integer representation of characters in the unicode format.
        char_position = ord(letter)
        #remove the shift key to the unicode integer
        new_position = (char_position - shift_key - 65) % 26 + 65
        # use the new integer to get the original character
        new_letter = chr(new_position)
        # add the new character to the original/normal text
        normal_text += new_letter
    elif letter.isdigit():
        char_position = ord(letter)
        new_position = (char_position - shift_key -48 ) % 10 + 48
        new_letter = chr(new_position)
        normal_text += new_letter       
    else:      
        # for lower characters
        char_position = ord(letter)
        new_position = (char_position - shift_key - 97) % 26 +97
        new_letter = chr(new_position)
        normal_text += new_letter

print(normal_text)