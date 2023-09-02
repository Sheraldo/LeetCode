"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
"""
def they_match(d1, d2):
    if len(d1) != len(d2):
        return False

    for k,v in d1.items():
        if k not in d2 or v != d2[k]:
            return False
    return True

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hashed_words = defaultdict(int)
        for w in words:
            hashed_words[hash(w)] += 1
        
        w_len = len(words[0])
        dict_len = len(words)
        window_len = w_len * dict_len

        win_s, win_e = 0, window_len - 1

        if win_e >= len(s):
            return []

        ans = []

        while win_e < len(s):
            matchin_piece = True
            curr_window_dict = defaultdict(int)
            for i in range(win_s, win_e + 1, w_len):
                cw = s[i:i + w_len]
                if hash(cw) not in hashed_words:
                    matchin_piece = False
                    break
                curr_window_dict[hash(cw)] += 1
            if matchin_piece and they_match(curr_window_dict, hashed_words):
                # matched, now check if exhausting all and is part of ans
                ans.append(win_s)
            win_s += 1
            win_e += 1
        
        return ans

