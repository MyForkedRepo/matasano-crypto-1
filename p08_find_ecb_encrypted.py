#  Detecting ECB
# 
# At the following URL are a bunch of hex-encoded ciphertexts:
# 
#    https://gist.github.com/3132928
# 
# One of them is ECB encrypted. Detect it.
# 
# Remember that the problem with ECB is that it is stateless and deterministic; the same
# 16 byte plaintext block will always produce the same 16 byte
# ciphertext.


from base64 import b64decode
from collections import Counter

if __name__ == '__main__':
    best_match_line = None
    best_match_score = 0
    
    with open('3132928/gistfile1.txt') as f:
        for line in f.readlines():
            line = line.strip()
            text = line.decode('hex')

            # Divide text into an array of 128 (16 bytes) bits each
            blocks = [text[(start*16) :
                           (start+1)*16] 
                        for start in xrange(len(text)/16)]

            block_count = Counter()
            for block in blocks:
                block_count[block] += 1

            # number of total repeating blocks is the score of the ecb encoded string
            repeating_blocks = 0
            for key, value in block_count.items():
                if value > 1:
                    repeating_blocks += value

            if repeating_blocks > best_match_score:
                best_match_score = repeating_blocks
                best_match_line = line

    print best_match_line
                
