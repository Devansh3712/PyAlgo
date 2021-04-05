"""
module for implementation
of Rabin Karp algorithm
for pattern searching
"""

CHAR = 256
  
def rabin_karp(pattern, text):

    """
    searches all occurences
    of pattern in text, returns
    list of indexes
    """

    PRIME 		= 101
    len_pat 	= len(pattern) 
    len_txt 	= len(text) 
    i 			= 0
    j 			= 0
    hash_pat	= 0
    hash_txt 	= 0 
    h 			= 1
    result 		= []

    for i in range(len_pat - 1): 
        h = (h * CHAR) % PRIME 

    for i in range(len_pat): 
        hash_pat = (CHAR * hash_pat + ord(pattern[i])) % PRIME 
        hash_txt = (CHAR * hash_txt + ord(text[i])) % PRIME 

    for i in range(len_txt - len_pat + 1): 

        if (hash_pat == hash_txt): 

            for j in range(len_pat):

                if (text[i + j] != pattern[j]): 
                    break

                else: 
                	j += 1

            if (j == len_pat): 
                result.append(i) 

        if (i < len_txt - len_pat): 
            hash_txt = (CHAR * (hash_txt - ord(text[i]) * h) + ord(text[i + len_pat])) % PRIME 

            if (hash_txt < 0): 
                hash_txt = hash_txt + PRIME

    return result

"""
PyAlgo
Devansh Singh, 2021
"""
