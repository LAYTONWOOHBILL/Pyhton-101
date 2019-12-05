###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows={}
    file = open(filename, 'r')
    for line in file:
        data=line.split(',')
        cow=data[0]
        ton=eval(data[1].replace('\n',''))
        cows[cow]=ton
    #print(cows)
    return(cows)
        
        
file_1='ps1_cow_data.txt'
file_2='ps1_cow_data_2.txt'

cows_1=load_cows(file_1)

'''
{'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2,
'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
'''

cows_2=load_cows(file_2)

'''
{'Miss Moo-dy': 3, 'Milkshake': 4, 'Lotus': 10, 'Miss Bella': 2, 'Horns': 9, 'Betsy': 5, 'Rose': 3, 'Dottie': 6}
'''

cows_3=load_cows(file_1)
cows_4=load_cows(file_2)


    
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    result = []
    cowsCopy = sorted(cows, key = cows.__getitem__,
                       reverse = True)
    #print(cowsCopy)
    #print(type(cows))
    while cows!={}:
        shiplst=[]
        totalTon=0
        for i in cowsCopy:
            #print(type(i))
            try:
                if cows.get(i) + totalTon <= limit:
                    shiplst.append(i)
                    totalTon+=cows.get(i)
            except:
                pass
        result.append(shiplst)
        for m in shiplst:
            cows.pop(m)
    #print('transport trip :{}'.format(result))
    return result
    
greedy_cow_transport(cows_1,limit=10)
'''
transport trip :

[['Betsy'], ['Henrietta'], ['Herman', 'Maggie'],
['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']]

'''
greedy_cow_transport(cows_2,limit=10)

'''
transport trip :

[['Lotus'], ['Horns'], ['Dottie', 'Milkshake'],
['Betsy', 'Miss Moo-dy', 'Miss Bella'], ['Rose']]

'''





# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    for partition in get_partitions(cows):
        #print(partition)
        block=[]
        for i in range(len(partition)):
            #print(i)
            x=0
            for j in partition[i]:
                x+=cows.get(j)
                #print(j,d.get(j))
                #print(x)
            #print(x)
            block.append(x)
        #print(block)
        if all(x <= limit for x in block):
            return partition
        
                

#a=brute_force_cow_transport(cows_3,limit=10)
'''

[['Henrietta'], ['Oreo', 'Maggie'], ['Milkshake', 'Moo Moo', 'Florence', 'Lola'], ['Millie'], ['Herman'], ['Betsy']]

'''

#b=brute_force_cow_transport(cows_4,limit=10)

'''

[['Rose', 'Dottie'], ['Horns'], ['Miss Moo-dy', 'Milkshake', 'Miss Bella'], ['Lotus'], ['Betsy']]

'''
#print(a)
#print(b)

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    timelist=[]
    start = time.time()
    cows=load_cows(file_1)
    greedy_cow_transport(cows,limit=10)
    ## code to be timed
    end = time.time()
    diff= end-start
    timelist.append(diff)

    start = time.time()
    cows=load_cows(file_1)
    brute_force_cow_transport(cows,limit=10)
    ## code to be timed
    end = time.time()
    diff= end-start
    timelist.append(diff)
    print(timelist)

#compare_cow_transport_algorithms()
'''
[0.00022125244140625, 0.7447240352630615]
'''

    
