####################################
####################################
# wget --header='User-Agent: Mozilla/5.0' 'http://www.gutenberg.org/cache/epub/35/pg35.txt' -c -O book.txt
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

from collections import Counter, defaultdict

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
encoded_string = hex_encoded_string.decode('hex')

def decode_xor_cipher(book_path):
    ''' Brute force a xor cipher '''
    char_map = get_char_frequency_from_file(book_path)

    scores = Counter()
    for char in char_map.keys():
        possible = xor_cipher(encoded_string, char)
        scores[char] = compare_character_frequency(Counter(possible), char_map)

    return xor_cipher(encoded_string, scores.most_common(1)[0][0]), scores.most_common(1)[0][1]

# Utility functions
def string_xor(x, y):
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(x,y)])

def xor_cipher(string, key):
    return string_xor(len(string) * key, string)

def get_char_frequency_from_string(string):
    return Counter(string)

def get_char_frequency_from_file(file_name):
    contents = open(file_name).read()
    return Counter(contents)

def compare_character_frequency(possible_map, reference_map):
    ''' A simplified edit distance comparison
        A score of the string is computed on the basis of how many consecutive pairs
        of the string are in order - i.e. character 1 of pair occurs more than
        character 2 of the pair - the number of occurences is the score match of the
        frequency maps
    '''

    # Get the frequency map as a string ordered by most common occuring first
    possible_map_sorted = ' '.join([x[0] for x in possible_map.most_common()])
    reference_map_sorted = ' '.join([x[0] for x in reference_map.most_common()])

    matches = 0
    prev_index = reference_map_sorted.find(possible_map_sorted[0])
    for char in possible_map_sorted[1:]:
        index = reference_map_sorted.find(char)
        if index != -1 and prev_index != -1 and index > prev_index:
            matches += 1
        prev_index = index

    return matches

if __name__ == '__main__':
    decoded_string, score = decode_xor_cipher('book.txt')
