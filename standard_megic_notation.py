class StandardMegicNotation:
    def __init__(self, note_vals_durs_1_meas=[("C", 1)]):
# First, check to see if the notes are less than one measure.  The current program cannot handle more than one measure.
        gt_1_meas = False
        for note_val_dur in note_vals_durs_1_meas:
            pass
# For every note's duration, we first convert into a string, which represents the binary value.
# 1 -> |0000.0001|0000.0000|
# 2 -> |0000.0000|1000.0000|
# 4 -> |0000.0000|0100.0000|
# 8 -> |0000.0000|0010.0000|
# 16-> |0000.0000|0001.0000|
# 32-> |0000.0000|0000.1000|
# 64-> |0000.0000|0000.0100|
# Note: the "."s are just there to help me to see which digit I'm on.  So the sum of all the notes must be <= 1/1, which in binary is "|0000.0001|0000.0000|".  I believe that in order to guarantee that the sum of the notes is  less than 1/1, I just add up the numbers as binary numbers,  and if the value is <= |0000.0001|0000.0000|,  then we're gravy.  So, let's add up a few notes to see what that looks like:  Let's start out with 2 half notes,  because they should add up to 1 whole note,  and therefore represent the upper limit.  1 half note, aka "2":
# 2 -> |0000.0000|1000.0000|
# The second half note, also aka "2":
# 2 -> |0000.0000|1000.0000|
# Now, if we use the normal rule of binary addition:  1/2  +  1/2  =
# 1/2 -> |0000.0000|1000.0000|  +
# 1/2 -> |0000.0000|1000.0000|  =
# 2/2 -> |0000.0000|2000.0000|  but binary does not allow the digit "2",  so we zero out 2 and carry 1 over,  =
# 1/1 -> |0000.0001|0000.0000|  So the first test works.  What about one half note and two quarter notes?
# 1/2 -> |0000.0000|1000.0000|  +
# 1/4 -> |0000.0000|0100.0000|  +
# 1/4 -> |0000.0000|0100.0000|  =
# 1/1 -> |0000.0000|1200.0000|  But again, binary digits do not accept "2",  so we zero out the 2 and carry over the 1:
# 1/1 -> |0000.0000|2000.0000|  But again, binary digits do not accept "2",  so we zero out the 2 and carry over the 1:
# 1/1 -> |0000.0001|0000.0000|  So the second test works out too.  The above explanations of binary addition suggest an algorithm:  Add up all the notes digit by digit, then, from right to left, carry over the extra "1"s until the current digit is either "1" or "0".  Then, repeat the same operation on the digit to the left of the current digit, until you've gotten to 1/1, or |0000.0001|0000.0000|.  The above discussion of what is needed to write a program that adds binary representations of numbers suggests that a recursive function.  Since we have an upper limit and a lower limit on the durations of the notes, we could solve the problem with nested for loops, but that is less elegant, and also, you can use this recursive function in the future, and it is a good exercise.
class Utils:
    def decimalNumbersToBinaryStrings(self, dec_num):
# Instead of trying to finish this function, I'm going to do something far simpler: powersOf2DecToBin()
        print("ERROR: decimalNumbersToBinaryStrings() is not implemented yet.")
        exit(1)
# dec_num can be a string or an integer.  What is returned, bin_str, is a string representation of a binary number.  Let's think aloud about this problem.  Suppose the input is 4.  How many times does 2 go into 4?  2 times.  What is the binary representation of the decimal number 4?  It is 100.  How do we get from "4" to "100"?  Since 2 goes into 4 2 times, could the rule be... Wait, let's start simpler.  Suppose the input is 1.  What should the output be?  "1" or "|0000.0001|0000.0000|" or some other form of how you write a binary number.
        dec_num = int(dec_num)
# Let's limit our numbers to be between 64 and 1/64, or "|0100.0000|0000.0000|" and "|0000.0000|0000.0100|".

    def zeroTo1DecToBin(self, decimalDenominator):
        # The goal of this function is to take in a decimal number that is some power of 2, but less than or equal to 0 (i.e., [1/64, 1/1]), and to output the binary representation as a string, that looks like "|0000.0001|0000.0000|".  As I am having trouble banging out the code, though it sounds so simple, I shall think aloud again.  Suppose the input is 64.  We want to output the binary representation of 1/64, which is "|0000.0000|0000.0100|".  There is a simple correspondence between these decimal fractions and their binary representations: 1/64 = 1/(2^6) =
# powers of 2:  7654 3210 1234 5678 <-- second 8 numbers are negative powers of 2.
# binary repr: |0000.0000|0000.0100|  Of course there is an extremely simple correspondence between these decimal fractions and their binary representations: that's how binary numbers are constructed.
        powerOfTwo = 0
        if decimalDenominator > 64 or decimalDenominator < 1:
            print("ERROR: decimal denominator '{}' must between [1, 64].".format(decimalDenominator))
            exit(1)
        elif decimalDenominator == 1:
            binary = "|0000.0001|0000.0000|"
        elif decimalDenominator == 2:
            binary = "|0000.0000|1000.0000|"
        elif decimalDenominator == 4:
            binary = "|0000.0000|0100.0000|"
        elif decimalDenominator == 8:
            binary = "|0000.0000|0010.0000|"
        elif decimalDenominator == 16:
            binary = "|0000.0000|0001.0000|"
        elif decimalDenominator == 32:
            binary = "|0000.0000|0000.1000|"
        elif decimalDenominator == 64:
            binary = "|0000.0000|0000.0100|"
        else:
            print("ERROR: decimal denominator '{}' must be a power of two.".format(decimalDenominator))
            exit(1)

        return binary

