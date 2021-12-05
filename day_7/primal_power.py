from day_7.check_prime import Solution as check_prime

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        prime_calculator = check_prime()
        count = 0
        for i in A:
            if i <= 1:
                continue
            if prime_calculator.isPrime(i):
                count += 1
                print(f"prime: ", i)

        print(count)
        return count


if __name__ == "__main__":
    obj = Solution()
    a = [ 999553, 999853, 999749, 999907, 999433, 999931, 999917, 999959, 999953, 999499, 999773, 999727, 999451, 0, 1,
          -100000, 2, -100001, 999953, 999809, 999959, 999553, 836180, 999883, 999809, 999491, 999907, 266720, 999599,
          999683, 999611, 999959, 999631, 999521, 492906, 793582, 999553, 999521, 999721, 999613, 999611, 999389, 999863,
          999389, 999671, 999983, 999853, 999763, 999499, 999653, 920713, 999599, 999683, 999809, 999611, 999563, 999809,
          999451, 999953, 999727, 999749, 999883, 936503, 999721, 999763, 999491, 999433, 999623, 999749, 999521, 999437, 999491, 290023, 999499, 999863, 727486, 999623, 999451, 999983, 999769, 999979, 999653, 999763, 999983, 999491, 999433, 999917, 999521, 999769, 999451, 999499, 999683, 999953, 999431, 999769, 999563, 999499, 999721, 999961, 999437, 999437, 999809, 999769, 999953, 999853, 999931, 671105, 999979, 649661, 999521, 999769, 999529, 516711, 999769, 999599, 274072, 999563, 999959, 999809, 480245, 999389, 999773, 886711, 999727, 740599, 999931, 999773, 417456, 492223, 999631, 999491, 999667, 999809, 999959, 999599, 651968, 999763, 999667, 999721, 999773, 999853, 999491, 999613, 999749, 999917, 999431, 999451, 999769, 999907, 999389, 275486, 999749, 999979, 580019, 999961, 999917, 999809, 735584, 329258, 467854, 999667, 999683, 999809, 999959, 999431, 999773, 999437, 497317, 999931, 999611, 802872, 999491, 999853, 999563, 291862, 213395, 999671, 970503, 999907, 999499, 699099, 587765, 554147, 999451, 656301, 999499, 999863, 613581, 999431, 999917, 999613, 999883, 999853, 999623, 999809, 999541, 881255, 999451, 999959, 999499, 999623, 999863, 978167, 999451, 999611, 999599, 999979, 999613, 999451, 999671, 999809, 999931, 813519, 999749, 999749, 999613, 934144, 999721, 999917, 999727, 251426, 999433, 999917, 999959, 563481, 999769, 999769, 999961, 999749, 999433, 999769, 999653, 999763, 999863, 532226, 999953, 999529, 415439, 522781, 999863, 999917, 999433, 999727, 999541, 999653, 999563, 999631, 437150, 999721, 417691, 999953, 784789, 999749, 999611, 999631, 999853, 999437, 999863, 942306, 999917, 505989, 999683, 999553, 999931, 334101, 999749, 999613, 999769, 999541, 999983, 999623, 999563, 845257, 999521, 999541, 999599, 999769, 999451, 999959, 999961, 999727, 999683, 999553, 999961, 999563, 999431, 999499, 999631, 999809, 999613, 999499, 999773, 999623, 999959, 999653, 999499, 999553, 808892, 999983, 999953, 494301, 999979, 999769, 999769, 999389, 764538, 999653, 999931, 999773, 999769, 999623, 999529, 999769, 999521, 999721, 999959, 999521, 792776, 305577, 954050, 999563, 999437, 999809, 999389, 574172, 999907, 999499, 999431, 999953, 999563, 216565, 999883, 999721, 999853, 214885, 567135, 344986, 816612, 999667, 999979, 999433, 999727, 291257, 999917, 750005, 999983, 999907, 999853, 999853, 999953, 999553, 638792, 479316, 999521, 999563, 999611, 219048, 999671, 999979, 999721, 605871, 999433, 895335, 694058, 455532, 999863, 354442, 428999, 999631, 999437, 999631, 999631, 707602, 999541, 492367, 999863, 999953, 999983, 999683, 999451, 999769, 999983, 999631, 999631, 999959, 999853, 999499, 408215, 999623, 376097, 999491, 999883, 999631, 999613, 999853, 999529, 999653, 691297, 999979, 734946, 999521, 999959, 999491, 999599, 374326, 999809, 999437, 999853, 999499, 999749, 999671, 999863, 999979, 999763, 999931, 999907, 999431, 999773, 999979, 999623, 999961, 999623, 999613, 426288, 999721, 999631, 999721, 999631, 999563, 999931, 999749, 999521, 999563, 999631, 472637, 999763, 304337, 844168, 999721, 999667, 999499, 999667, 999667, 481339, 999863, 999809, 999959, 999883, 999961, 999553, 495632, 999917, 999599, 999917, 999553, 999809, 999961, 999883, 999769, 999683, 999437, 999491, 999491, 999521, 999721, 999599, 967435, 447008, 999953, 999959, 999763, 999529, 778063, 999721, 999727, 999623, 999749, 999437, 999491, 999979, 999499, 999491, 999769, 999521, 999563, 999451, 999653, 999721, 999623, 999763, 999883, 999683, 673349, 368182, 999613, 999809, 999613, 999389, 999389, 999961, 999529, 999611, 999667, 999979, 999431, 999563, 999883, 999961, 999431, 538996, 999437, 999917, 999931, 999721, 999623, 999853, 999809, 999763, 891589, 999599, 999667, 999961, 999389, 999529, 999809, 999499, 446427, 999433, 193330, 999931, 999389, 316531, 999389, 999853, 999491, 999611, 999883, 999727, 999907, 999451, 884091, 999451, 999529, 999653, 999727, 462934, 999451, 301780, 999863, 999917, 999431, 999773, 999521, 376401, 999853, 339530, 358779, 251915, 477884, 659978, 999721, 999389, 999431, 999763, 999623, 999433, 999613, 999499, 999667, 999563, 999853, 999541, 999979, 307209, 583190, 878096, 999983, 999979, 999863, 999931, 999437, 999931, 999611, 999433, 999389, 999809, 999959, 829197, 707419, 999667, 999727, 999983, 999769, 975718, 999749, 999671, 999613, 455226, 228256, 999599, 999623, 999979, 999491, 999683, 999599, 999883, 999563, 999769, 999683, 999883, 489025, 999521, 688256, 999431, 529222, 999979, 999749, 999773, 999763, 999653, 999853, 894159, 999983, 321657, 999749, 999541, 999953, 999389, 999437, 491205, 999611, 426594, 999979, 999809, 999611, 999599, 999883, 999431, 999499, 999721, 215604, 999983, 999721, 999389, 999853, 999917, 999721, 999883, 999433, 999959, 999521, 614228, 299558, 803168, 999389, 999553, 999671, 233165, 999721, 999499, 999953, 999883, 999623, 999563, 388833, 999953, 999727, 999727, 999863, 999433, 999883, 999671, 999749, 999521, 999863, 999683, 999749, 869075, 999769, 999541, 999553, 999763, 392316, 525489, 999631, 999529, 999727, 999931, 648152, 999809, 740653, 999529, 999683, 256721, 999599, 999853, 999499, 999521, 999563, 999451, 999613, 999431, 898092, 999863, 999763, 999521, 999491, 934206, 999631, 999809, 999727, 999553, 999623, 999433, 999389, 999863, 329991, 999433, 991441, 999917, 397531, 999623, 999721, 999907, 999541, 502290, 999931, 999437, 999853, 999389, 999667, 999553, 999917, 999863, 999437, 999437, 702724, 999863, 999853, 999437, 999769, 999521, 595126, 999529, 999671, 999433, 999671, 999749, 999389, 999521, 742540, 999437, 999727, 999749, 999553, 999431, 999671, 895747, 968352, 857298, 999953, 344085, 999653, 999613, 999499, 999863, 674894, 264033, 728031, 999491, 999653, 999769, 553698, 318009, 459055, 999931, 999721, 999529, 409934, 999863, 589891, 999727, 999683, 894282, 999563, 999667, 999553, 206066, 999541, 999541, 999431, 999979, 999917, 999763, 999553, 999521, 999437, 999763, 999749, 704996, 999433, 999653, 465109, 999623, 999563, 757867, 999917, 377614, 999727, 214786, 999959, 999521, 999961, 999433, 999763, 999433, 999863, 880073, 999671, 999451, 999763, 999809, 999721, 999979, 501192, 999499, 999931, 999721, 999451, 999623, 601962, 999721, 999907, 999631, 999437, 568468, 999721, 999553, 999763, 626701, 999727, 999529, 999671, 999917, 999433, 999907, 999563, 999907, 999529, 999451, 999499, 999563, 999721, 999431, 999931, 999433, 999883, 438333, 999773, 999763, 999623, 999451, 999433, 999437, 999529, 999667, 999491, 999529, 999611, 999623, 295637, 767845, 999931, 999613, 999953, 853932, 999563, 999563, 999529, 999521, 999983, 999961, 999763, 999917, 999809, 999499, 999773, 999683, 999431, 592580, 999671, 999959, 999437, 999671, 814896, 331644, 442498, 999769, 999809, 999553, 234531, 999749, 999907, 999773, 999721, 999671, 999433, 999451, 218925, 999809, 479570, 999917, 999553, 999983, 999979, 999763, 999959, 999541, 999763, 388747, 999863, 999529, 999599, 999953, 999683, 999959, 927616, 999563, 999611, 411642, 999499, 595973, 999631, 999763, 383817, 860640, 999917, 897655, 315646, 999521, 999529, 999389, 999599, 999433, 999631, 999931, 542852, 999433, 999389, 999671, 999769, 401917, 999749, 999853, 999433, 999931, 285870, 999883, 361943, 499767, 607157, 999431, 999773, 594758, 999931, 444096, 314496, 999431, 999763, 389095, 682625, 999611, 999653, 999883, 671346, 737694, 999773, 999623, 999959, 590626, 999749, 999623, 999917, 629010, 999521, 999959, 696737, 999451, 999433, 999541, 999599, 999499, 800417, 999763, 544357, 999667, 999499, 999721, 999961, 999563 ]
    obj.solve(a)
