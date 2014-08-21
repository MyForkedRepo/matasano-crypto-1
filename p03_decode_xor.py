####################################
####################################
# wget --header='User-Agent: Mozilla/5.0' 'http://www.gutenberg.org/cache/epub/19033/pg19033.txt' -c -O book.txt
###################################
###################################

# Single-character XOR Cipher
# 
# The hex encoded string:
# 
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# 
# ... has been XOR'd against a single character. Find the key, decrypt
# the message.
# 
# Write code to do this for you.
# 
# Here's one way:
# 
# a. Find a large sample of English text. Something from Project
# Gutenberg should do nicely. Use it to generate a character frequency
# map. (Do not restrict this to alphanumeric characters! Whitespace is
# more common than any of them in English text.)
# 
# b. Evaluate each potential key by scoring the resulting plaintext
# against the frequency map. The key with the best score is your match.

from collections import Counter
import string

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
encoded_string = hex_encoded_string.decode('hex')

def decode_xor_cipher(char_map, encoded_string):
    ''' Brute force a xor cipher '''

    scores = Counter()
    for char in char_map.keys():
        possible = xor_cipher(encoded_string, char)
        scores[char] = compare_character_frequency(Counter(possible), char_map)

    least_score = scores.most_common()[-1]
    key, score = least_score[:]
    return xor_cipher(encoded_string, key), score, key

# Utility functions
def string_xor(x, y):
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(x, y)])

def xor_cipher(string, key):
    return string_xor(len(string) * key, string)

def get_char_frequency_from_string(string):
    c = Counter(string)
    for k, v in c.items():
        c[k] = v * 1.0 / len(string)
    return c

def get_char_frequency_from_file(file_name):
    contents = open(file_name).read()
    return get_char_frequency_from_string(contents)

def compare_character_frequency(possible_map, reference_map):
    ''' A score of the string is computed based on the sum of absolute difference of character
        frequencies between the two maps. Least score is the best score
    '''

    character_set = ''.join(reference_map.keys()) + string.letters + string.digits
    possible_map_set = ''.join(possible_map)
    # Ignore strings which have characters other than reference map
    if len(possible_map_set.strip(character_set)) > 0:
        return 1000

    score = 0
    for char, freq in possible_map.items():
        reference_freq = reference_map[char]
        score += abs(reference_freq - freq)

    return score

if __name__ == '__main__':
    reference_map = get_char_frequency_from_file('book.txt')
    decoded_string, score, character = decode_xor_cipher(reference_map, encoded_string)
    print decoded_string
