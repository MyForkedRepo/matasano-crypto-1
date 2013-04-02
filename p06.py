##################################
##################################
# https://gist.github.com/3132752.git
##################################
##################################

# Break repeating-key XOR
# 
# The buffer at the following location:
# 
#  https://gist.github.com/3132752
# 
# is Base64-encoded repeating-key XOR. Break it.
# 
# Here's how:
# 
# a. Let KEYSIZE be the guessed length of the key; try values from 2 to
# (say) 40.
# 
# b. Write a function to compute the edit distance/Hamming distance
# between two strings. The Hamming distance is just the number of
# differing bits. The distance between:
# 
#  this is a test
# 
# and:
# 
#  wokka wokka!!!
# 
# is 37.
# 
# c. For each KEYSIZE, take the FIRST KEYSIZE worth of bytes, and the
# SECOND KEYSIZE worth of bytes, and find the edit distance between
# them. Normalize this result by dividing by KEYSIZE.
# 
# d. The KEYSIZE with the smallest normalized edit distance is probably
# the key. You could proceed perhaps with the smallest 2-3 KEYSIZE
# values. Or take 4 KEYSIZE blocks instead of 2 and average the
# distances.
# 
# e. Now that you probably know the KEYSIZE: break the ciphertext into
# blocks of KEYSIZE length.
# 
# f. Now transpose the blocks: make a block that is the first byte of
# every block, and a block that is the second byte of every block, and
# so on.
# 
# g. Solve each block as if it was single-character XOR. You already
# have code to do this.
# 
# e. For each block, the single-byte XOR key that produces the best
# looking histogram is the repeating-key XOR key byte for that
# block. Put them together and you have the key.

from base64 import b64decode
from p03 import decode_xor_cipher, get_char_frequency_from_file
from p05 import repeating_key_xor_cipher
from operator import itemgetter

def guess_key_size(text):
    ''' Guess the key size using c. and d. above '''
    distances = []
    for key_size in xrange(2, 40):
        # Tried two approaches here
        # Taking the whole text gives the minimum keysize as the answer on the top, but it might 
        # be prohibitive for large texts

        # Whole text approach
        # blocks = [text[:-key_size], text[key_size:]]

        # Take 8 blocks
        blocks = [text[start*key_size:
                       (start+1) * key_size] for start in xrange(8)]


        avg_distance = 0
        for i in xrange(1, len(blocks), 2):
            avg_distance += hamming_distance(blocks[i], blocks[i-1]) * 1.0
        avg_distance /= len(blocks)/2

        normalised_distance = avg_distance / len(blocks[0])

        distances.append([normalised_distance, key_size])

    sorted_distances = sorted(distances, key = itemgetter(0))

    best_keysizes = [i[1] for i in sorted_distances]
    return best_keysizes[:5]

def decode_repeating_key_xor(text, reference_map):
    ''' Main function to decode a repeating key xor '''
    key_sizes = guess_key_size(text)
    blocks = []

    best_key = None
    best_score = 0

    for key_size in key_sizes:
        score = 0
        key = ''
        for start in xrange(key_size):
            block = text[start::key_size]
            decoded_string, block_score, block_key = decode_xor_cipher(reference_map, block)
            score += block_score
            key += block_key
        if score > best_score:
            best_score = score
            best_key = key
    
    return repeating_key_xor_cipher(text, best_key)

def hamming_distance(s1, s2):
    return sum(bit_count(ord(ch1) ^ ord(ch2)) for ch1, ch2 in zip(s1, s2))

def bit_count(n):
    if n == 0:
        return 0
    return 1 + bit_count(n & (n - 1))

if __name__ == '__main__':
    reference_map = get_char_frequency_from_file('book.txt')

    f = open('3132752/gistfile1.txt')
    b64_text = f.read()
    text = b64decode(b64_text)

    print decode_repeating_key_xor(text, reference_map)
