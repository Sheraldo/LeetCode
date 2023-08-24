"""
https://leetcode.com/problems/text-justification/description/

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cline, clen = [], 0
        i = 0

        while i < len(words):

            if clen + len(cline) + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - clen
                spaces = extra_spaces // max(1, len(cline) - 1)
                remainder = extra_spaces % max(1, len(cline) - 1)

                for j in range(max(1, len(cline) - 1)):
                    cline[j] += " " * spaces
                    if remainder:
                        cline[j] += " "
                        remainder -= 1

                ans.append("".join(cline))
                cline, clen = [], 0

            cline.append(words[i])
            clen += len(words[i])
            i += 1

        # last line
        last_line = " ".join(cline)
        trail_spaces = maxWidth - len(last_line)
        last_line += " " * trail_spaces
        ans.append(last_line)

        return ans

