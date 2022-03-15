# Huffman decoding
# Part 1.
#     Given the following list of codes: ["l\t000", "d\t1111", "h\t1001", "o\t0010", "r\t1010", "w\t1110", "e\t1100", " \t1011", "\n\t1101"]
#     Decode the following encoded string:    "100111000000000010101111100010101000011111101".
#     Return the decoded string.
#
# Part 2.
#     Write a function to decode any valid encoded string, given any list of codes.
#
def decode(codes_list, encoded_string):
 
 
    # create a map
    # {000: l, 1111:d ...}
    codes_map = {}
    # codes_map["000"] = "l"
    # iterate through codes_list, split each code into 2 parts: character, binaryString
    for i in range(len(codes_list)):
        code = codes_list[i]
        character = code[0]
        binary = code[2:]
        codes_map[binary] = character
        
    
    # iterate through encoded_string
    temp = ""
    result = ""
    for num in encoded_string:
        temp += num
        if temp in codes_map:
            result += codes_map[temp]
            temp = ""
        
    return result
 
    
 
codes = ["l\t000", "d\t1111", "h\t1001", "o\t0010", "r\t1010", "w\t1110", "e\t1100", " \t1011", "\n\t1101"]
encoded = "100111000000000010101111100010101000011111101"
print(decode(codes, encoded))
 
 
# Assumptions & Requirements
# * <character><delimiter><binaryString>
# * delimiter = \t
# * 000000 => ll
# * binaryString length >= 1
# * 
