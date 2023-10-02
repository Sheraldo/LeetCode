"""
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/?envType=daily-question&envId=2023-10-02

Example 1:

Input: colors = "AAABABB"
Output: true
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.

Example 2:

Input: colors = "AA"
Output: false
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.

Example 3:

Input: colors = "ABBBBBBBAAA"
Output: false
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.



Constraints:

    1 <= colors.length <= 105
    colors consists of only the letters 'A' and 'B'

"""
def get_color_sequences(colors, c) -> list:
    i = 0
    n = len(colors)
    seq = []
    while i < n:
        if colors[i] == c:
            j = i
            cnt = 0
            while j < n and colors[j] == c:
                cnt += 1
                j += 1
            seq.append(cnt)
            i = j
        i += 1
    return seq
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_seq = get_color_sequences(colors, 'A')
        b_seq = get_color_sequences(colors, 'B')

        a_valid = [cnt - 2 for cnt in a_seq if cnt > 2]
        b_valid = [cnt - 2 for cnt in b_seq if cnt > 2]

        a_moves = sum(a_valid)
        b_moves = sum(b_valid)

        # print(f"{a_moves=}, {b_moves=}")
        i = 0
        while a_moves and b_moves:
            if i % 2 == 0:
                a_moves -= 1
            else:
                b_moves -= 1
            i += 1
        if i%2 == 0:
            return  True if a_moves else False
        else:
            return False if b_moves else True

