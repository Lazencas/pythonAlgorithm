hash_table = [0 for i in range(5)]
hash_address = 0

def get_key(data):
    return hash(data)

def hashfunc(key):
    return key%5

def get_address(data):
    hash_address = hashfunc(get_key(data))

def write(data, value):
    hash_address = hashfunc(get_key(data))
    if hash_table[hash_address]!=0:
        while hash_table[hash_address]!=0:
                if hash_table[hash_address] !=0:
                    hash_table[hash_address] = value
                hash_address +=1
        return 
    hash_table[hash_address] = value

def read(data):
    hash_address = hashfunc(get_key(data))
    print(hash_table[hash_address])

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

a = hash(data1)

b=hashfunc(get_key(data1))
c=hashfunc(get_key(data2))
d=hashfunc(get_key(data3))
e=hashfunc(get_key(data4))

write(data1,1488)
write(data2,2222)

# hash_address = hashfunc(get_key(data3))
# while hash_table[hash_address]!=0:
#         if hash_table[hash_address] !=0:
#             hash_table[hash_address] = value
#         hash_address +=1



write(data3,3333)
write(data4,4444)        

for i in hash_table:
    print(i)
