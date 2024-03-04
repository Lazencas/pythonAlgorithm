hash_table = [0 for i in range(10)]
data = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'


indexkey = get_key(data)
hash_address = hash_function(indexkey)
if hash_table[hash_address] != 0:
    for idx in range(len(hash_table[hash_address])):
        if hash_table[hash_address][idx][0]==indexkey:
            hash_table[hash_address][idx][1] = value

        
    hash_table[hash_address].append([indexkey, value])

else:
    type(([indexkey, value]))
    hash_table[hash_address]=([indexkey, value])