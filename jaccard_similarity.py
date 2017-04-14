import metapy

def compute_jaccard(sentence1, sentence2):
    '''
    1) count the number of members which are shared between both sets
    2) count the total number of members in each set (words_union)
    3) divide the number of shared members (1) by the total number of members (2)
    4) multiply that number (3) by 100

    this percentage tells you how similar the two sets are
    '''

    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    words_union = len(words1) + len(words2)
    for word1 in words1:
        for word2 in words2:
            if word1 == word2:
                words_union -= 1
                break

    words_intersection = len(words1) + len(words2) - words_union
    similarity_percentage = (words_intersection / words_union) * 100
    return similarity_percentage