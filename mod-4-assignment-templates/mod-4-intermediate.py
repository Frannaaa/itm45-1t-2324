'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
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
    if letter == " ":
        return " "
    
    shifted_value = ord(letter) + shift
    
    while shifted_value > ord('Z'):
        shifted_value -= 26
    
    while shifted_value < ord('A'):
        shifted_value += 26
    
    return chr(shifted_value)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
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
         def shift_letter(letter, shift):
        if letter == " ":
            return " "
        
        shifted_value = (ord(letter) - ord('A') + shift) % 26
        return chr(shifted_value + ord('A'))
    
    return ''.join([shift_letter(char, shift) for char in message])

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
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
     if letter == " ":
        return " "
    
    # Convert the letter_shift into its corresponding shift value
    shift_value = ord(letter_shift) - ord('A')
    
    # Apply the shift to the letter
    shifted_value = (ord(letter) - ord('A') + shift_value) % 26
    return chr(shifted_value + ord('A'))

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
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
      # Extend the key to match the length of the message (ignoring spaces)
    extended_key = ''
    key_index = 0
    for char in message:
        if char != ' ':
            extended_key += key[key_index]
            key_index = (key_index + 1) % len(key)
        else:
            extended_key += ' '
    
    # Encrypt the message using the extended key
    encrypted_message = ''
    for i in range(len(message)):
        if message[i] == ' ':
            encrypted_message += ' '
        else:
            shift_value = ord(extended_key[i]) - ord('A')
            shifted_char = (ord(message[i]) - ord('A') + shift_value) % 26
            encrypted_message += chr(shifted_char + ord('A'))
    
    return encrypted_message
