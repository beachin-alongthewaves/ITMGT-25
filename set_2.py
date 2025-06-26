'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_letter(letter, shift):
        if letter == " ": # checks if the letter is a space
            return " " # if it is, return a space

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # defines a string called the alphabet with uppercase English letters in order

        for i in range(len(alphabet)): # loops through each index in the alphabet
            if alphabet[i] == letter: # if the letter at index i equals the input letter
                new_index = (i + shift) % 26 # calculates the updated index by adding the shift and wrapping around Z to A using % 26 (modulo)
                return alphabet[new_index] # returns the letter at the updated index

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def caesar_cipher(message, shift):
        encryption = "" # initializes the empty string to build the encrypted message onto
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # defines a string containing all uppercase English letters

        for i in message: # loops through each character in the input message
            if i == " ": # if the character is a space
                encryption += " " # then it keep it as a space, and add it to the encryption
            else: # otherwise, if the character is a letter
                index = alphabet.find(i) # find the index of the character in the alphabet string
                updated_index = (index + shift) % 26 # updates the index by adding the shift and wrapping around Z to A using % 26 (modulo)
                encryption += alphabet[updated_index] # adds the shifted character to the encryption string

        return encryption # returns the final encrypted message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_by_letter(letter, letter_shift):
        if letter == " ": # checks if the letter is a space
            return " " # if it is, return a space

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # defines a string containing all uppercase English letters
        shift = alphabet.find(letter_shift) # defines the variable shift based on the index of letter_shift in the alphabet

        for i in range(len(alphabet)): # loops through each index in the alphabet
            if alphabet[i] == letter: # if the letter at index i equals the input letter
                updated_index = (i + shift) % 26 # updates the index by adding the shift (based on letter_shift) and wrapping around Z to A using % 26 (modulo)
                return alphabet[updated_index] # returns the letter at the updated index

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def vigenere_cipher(message, key):
        encryption = "" # initializes the empty string to build the encrypted message onto
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # defines a string containing all uppercase English letters
        key_index = 0 # advances for every character in the message, used as a counter to track which index we are in the key
        key_length = len(key) # stores the length of the key, used to wrap around with a modulo

        for i in message: # loops through each character in the input message 
            key_char = key[key_index % key_length]  # defines which key character to apply to the specific letter in the message, indexes the character by using a modulo
            shift = alphabet.find(key_char) # defines the shift amount based on key_char

            if i == " ": # checks if the letter is a space
                encryption += " "  # if it is, then it keep it as a space, and add it to the encryption
            else: # otherwise, if the character is a letter
                i_index = alphabet.find(i) # identifies the index of the specific letter in the alphabet
                updated_index = (i_index + shift) % 26 # updates the index by adding the shift and wrapping around Z to A using % 26 (modulo)
                encryption += alphabet[updated_index] # adds the shifted character to the encryption string

            key_index += 1  #advances the key_index forward for every message character, even spaces

        return encryption # returns the final encrypted message

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def scytale_cipher(message, shift):
        
        while len(message) % shift != 0: # loops through the length of the message to check if it is divisible by the shift (if the remainder is not equal to 0) 
            message += "_" # if the remainder is not equal to 0, then add an underscore, increasing the length of the message, then checks again

        encryption = "" # initializes the empty string to build the encrypted message onto
        columns = len(message) // shift # calculates how many columns we have using the message length and shift

        for i in range(len(message)): # loops through each character's index in the input message
            col_index = i % shift # (i % shift) tells us what column we're on
            row_index = i // shift # (i // shift) tells us what row we're on
            updated_index = col_index * columns + row_index # updates the index by multiplying the columns by the column index, then adding the row index             
                # multiply col_index by columns to calculate how many characters we've passed, because each row has column characters
            encryption += message[updated_index] # adds the chosen indexed character to the encryption string

        return encryption # returns the final encrypted message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def scytale_decipher(message, shift):
        
        columns = len(message) // shift  # calculates how many columns we have using the message length and shift
        decryption = [''] * len(message) # initializes the empty string with len(message) length to build the decrypted message onto
            # *len(message) creates a list with len(message) elements, this allows us to index certain positions in the string to add decrypted letters onto as the code moves along

        for i in range(len(message)): # loops through each character's index in the input message
            row_index = i % shift # (i % shift) tells us what row we're on
            col_index = i // shift # (i // shift) tells us what column we're on
            updated_index = row_index * columns + col_index # updates the index by multiplying the columns by the row index, then adding the column index 
            decryption[updated_index] = message[i] # places the character to its correct position in the decryption string

        return ''.join(decryption) # returns the final decrypted message and combines them into a string