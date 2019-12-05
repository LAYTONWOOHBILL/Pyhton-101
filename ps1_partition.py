# From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]



'''
d={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Wilson':1}

def brute_force_cow_transport(cows,limit=10):
    for partition in get_partitions(d):
        #print(partition)
        block=[]
        for i in range(len(partition)):
            #print(i)
            x=0
            for j in partition[i]:
                x+=d.get(j)
                #print(j,d.get(j))
                #print(x)
            #print(x)
            block.append(x)
        #print(block)
        if all(x <= limit for x in block):
            return partition
            
print(brute_force_cow_transport(d)) 
'''        
                
       


