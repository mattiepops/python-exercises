import string
import re

#Create a translation table to do Atbash encoding
# 1. All ASCII letters (lower and uppercase)
# 2. Are translated into reversed lowercase letters, and
# 3. All whitespace and punctuation is removed
ENCODE_TABLE = str.maketrans(
    string.ascii_letters,
    "".join(reversed(string.ascii_lowercase + string.ascii_lowercase)),
    string.punctuation + string.whitespace
)

# Create a translation table to undo Atbash encoding
# 1. All lowercase ASCII letters
# 2. Are translated into the reversed lowercase letters, and
# 3. All whitespace is removed

DECODE_TABLE = str.maketrans(
    string.ascii_lowercase,
    ''.join(reversed(string.ascii_lowercase)),
    string.whitespace
)
def encode(plainstring):
    newstr = plainstring.translate(ENCODE_TABLE)
    result = re.findall(r'.{1,5}', newstr)
    return ' '.join(result)

def decode(encryptedstring):
    return encryptedstring.translate(DECODE_TABLE)