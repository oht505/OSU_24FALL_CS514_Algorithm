from hw6 import editDistance

start_string = ""
end_string = ""
if 0 != editDistance(start_string, end_string):
    raise Exception("Failed test")


start_string = "somestring"
end_string = "somestring"
if 0 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "dog"
end_string = "cow"
if 2 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "babble"
end_string = "apple"
if 3 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "ATCAT"
end_string = "ATTATC"
if 2 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"
end_string = "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"
if 11 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "CGCAATTCTGAAGCGCTGGGGAAGACGGGT"
end_string = "TATCCCATCGAACGCCTATTCTAGGAT"
if 18 != editDistance(start_string, end_string):
    raise Exception("Failed test")

start_string = "tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa"
end_string = "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt"
if 112 != editDistance(start_string, end_string):
    raise Exception("Failed test")

