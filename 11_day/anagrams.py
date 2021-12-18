class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        anagram_dict = dict()

        for i in range(len(A)):
            string = ''.join(sorted(A[i]))
            if string not in anagram_dict:
                anagram_dict[string] = [i + 1]
            else:
                anagram_dict[string].append(i+1)

        return list(anagram_dict.values())


if __name__ == "__main__":
    obj = Solution()
    a = ['cat', 'dog', 'god', 'tca']
    print(obj.anagrams(a))
