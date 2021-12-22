class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if len(A) == 1:
            return 1
        hash_map = dict()
        i = 0
        j = 0
        ans = 0
        while j < len(A):
            if A[j] not in hash_map:
                hash_map[A[j]] = 1
            else:
                ans = max(ans, j - i)
                while A[i] != A[j] and i < j:
                    i += 1
                i += 1
            j += 1
        ans = max(ans, j - i)
        return ans


if __name__ == "__main__":
    obj = Solution()
    a = "VXu9c01gYRAz7oIAxN3zKZb64EFKssfQ4HW971jv3H7x5E9dAszA0HrKTONyZDGYtHWt4QLhNsIs8mo4AIN7ecFKewyvGECAnaJpDn1MTTS4yTgZnm6N6qnmfjVt6ZU51F9BxH0jVG0kovTGSjTUkmb1mRTLQE5mTlVHcEz3yBOh4WiFFJjKJdi1HBIBaDL4r45HzaBvmYJPlWIomkqKEmQ4rLAbYG7C5rFfpMu8rHvjU7hP0JVvteGtaGn7mqeKsn7CgrJX1tb8t0ldaS3iUy8SEK"
    print(obj.lengthOfLongestSubstring(a))
