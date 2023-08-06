class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = int(1e9+7)
        dp = [[-1 for i in range(110)] for j in range(110)]

        def solve(plen, songs_used) -> int:
            if plen == goal:
                return songs_used == n

            if dp[plen][songs_used] != -1: return dp[plen][songs_used]

            # select next song from already used songs
            ans = (solve(plen + 1, songs_used) * max(0, songs_used - k)) % mod

            # select new song and add to playlist
            ans = (ans + solve(plen + 1, songs_used + 1) * (n - songs_used)) % mod

            dp[plen][songs_used] = ans
            return dp[plen][songs_used]

        return solve(0,0)
