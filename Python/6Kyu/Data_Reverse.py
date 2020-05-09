# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed.

def data_reverse(data):
    bytes_list = []
    for i in range(0,len(data), 8):
        bytes_list.append(data[i:i+8])
    r_bytes_list = bytes_list[::-1]
    r_data = []
    for b in r_bytes_list:
        for n in b:
            r_data.append(n)
    return r_data

#     Community Solution
#
# def data_reverse(data):
#     res = []
#     for i in range(len(data) - 8, -1, -8):
#         res.extend(data[i:i + 8])
#     return res
