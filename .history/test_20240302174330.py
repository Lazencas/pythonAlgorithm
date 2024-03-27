hash_table = [0 for i in range(10)]



def get_key(data):
    return hash(data)

def hash_function(key):
    return key%8

def get_address(data):
    hash_address = hashfunc(get_key(data))

def write(data, value):
    indexkey = get_key(data)
    hash_address = hash_function(indexkey)
    if hash_table[hash_address] != 0:
        for idx in range(len(hash_table[hash_address])):
            if hash_table[hash_address][idx][0]==indexkey:
                hash_table[hash_address][idx][1] = value
                return
            
        hash_table[hash_address].append([indexkey, value])
    
    else:
        type(([indexkey, value]))
        hash_table[hash_address]=([indexkey, value])

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

a = hash(data1)

b=hash_function(get_key(data1))
c=hash_function(get_key(data2))
d=hash_function(get_key(data3))
e=hash_function(get_key(data4))

write(data1,1488)
write(data2,2222)

# hash_address = hashfunc(get_key(data3))
# while hash_table[hash_address]!=0:
#         if hash_table[hash_address] !=0:
#             hash_table[hash_address] = value
#         hash_address +=1



write(data3,3333)
write(data4,4444)        
