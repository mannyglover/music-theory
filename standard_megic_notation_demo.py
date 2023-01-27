import standard_megic_notation as smn

sMN = smn.StandardMegicNotation()
utils = smn.Utils()
decimal = 32
binary = utils.zeroTo1DecToBin(decimal)

print("decimal denominator: {}\nbinary: {}".format(decimal, binary))
