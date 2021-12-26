class Solution:
    # @param A : string
    # @return a strings
    def string_reverse(self, string):
        result = ""
        for i in range(len(string)-1, -1, -1):
            result = result + string[i]
        return result

    def solve(self, A):
        reverse_sentence = self.string_reverse(A)
        string_array = reverse_sentence.split(' ')

        for i in range(len(string_array)):
            string_array[i] = self.string_reverse(string_array[i])

        return ' '.join(string_array)


if __name__ == "__main__":
    obj = Solution()
    sent = "this is a sentence"
    print (obj.solve(sent))