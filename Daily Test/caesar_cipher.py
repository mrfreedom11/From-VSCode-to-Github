# Caesar Cipher Shifted Alphabet Generator
alphabet = 'abcdefghijklmnopqrstuvwxyz' # Original alphabet
shift = 2 # Number of positions to shift
shifted_alphabet = alphabet[shift:] + alphabet[:shift] # Shifted alphabet + the start of the alphabet
print(shifted_alphabet) # Output: 'fghijklmnopqrstuvwxyzabcde'