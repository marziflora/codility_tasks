#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Min int not present in A
def solution(A):
    positive_A = set(sorted([a for a in A if a >0]))
    smallest_int = 1
    while smallest_int in positive_A:
        smallest_int +=1
    return smallest_int


# In[2]:


A = [-5, -7, -9]
solution(A)


# In[3]:


A = [1, 3, 6, 4, 1, 2, -5]
solution(A)


# In[7]:


# Max size of square made of 2 sticks A and B
def solution(A, B):
    bigger_int, smaller_int = max(A,B), min(A,B)
    possibilities = []
    
    for i in range(int(smaller_int/2),bigger_int+1 ): #liczba wynikowa
        if int(smaller_int) >= int(i*2) and bigger_int>= i*2 :
            possibilities.append(i)
        if int(smaller_int) >= int(i*1) and bigger_int>= i*3:
            possibilities.append(i)
    
    return max(possibilities)

print(solution(21,10)) # 7
print(solution(13,11)) # 5
print(solution(2,1))


# In[209]:


def return_last_position(position, blocks, reverse=False):
    last = blocks[position]
    j=0
    if reverse:
        blocks = blocks[:position]
        blocks = blocks[::-1]
        for j, i in enumerate(blocks):
            if i>= last:
                last = blocks[j]
                continue
            else:
                return position-j
        return 0
    else:
        for j, i in enumerate(blocks[position+1:]):
            if i>= last:
                last = blocks[j]
                continue
            else:
                return position+j
    return position+j+1


# In[210]:


#Blocks is array of stick heights. 2 frogs can move only on higher stick. 
#Present 2 frogs starts from random position and want to be as far as they can from each other
#How is the maximum distance they can be from each other starting from one point?
import numpy as np

def solution(blocks):
    possibilities = []
    for start_pos in range(0,len(blocks)):
        if start_pos==0:
            end_position = return_last_position(start_pos, blocks)
#             print(start_pos, end_position)
            possibilities.append(end_position-start_pos+1)
        elif start_pos==(len(blocks)-1):
            end_position = return_last_position(start_pos, blocks, reverse=True)
#             print(start_pos, end_position)
            possibilities.append(end_position-start_pos+1)
        else:
            end_position1 = return_last_position(start_pos, blocks, reverse=True)
            end_position2 = return_last_position(start_pos, blocks, reverse=False)
#             print(start_pos, end_position1, end_position1)
            possibilities.append(end_position2-end_position1+1)
    return max(possibilities)

blocks = np.array([1,1]) # return 2
print(blocks, solution(blocks))
blocks = np.array([1,5,5,2,6]) # return 4
print(blocks, solution(blocks))
blocks = np.array([2,6,8,5]) # return 3
print(blocks, solution(blocks))

