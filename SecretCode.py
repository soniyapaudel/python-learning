# Write a python program to translate message into secret code language.
# Use the rules below to translate normal English into secret code language

# coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the 
# end  now append three random characters at the starting and the end

# else:
#  simply reverse the string 
# 
# decoding:
# if the word contains less than 3 characters, reverse it 
# else:
# remove 3 random characters from start to end. Now remove the last letter and 
# append it to the beginning


#--- If...Else in one line

# a = 330
# b = 33
# print("A") if a>b else print("=") if a==b else print("B")

import random
import string

def random_string(length=3):
    return ''. join(random.choice(string.ascii_letters) for _ in range(length) )


st = input("Enter message:")
words = st.split()
coding = input("1 for Coding or 0 for Decoding:") # false for decoding and true for encoding 
coding = True if(coding == "1") else False 
if(coding):
    nwords = []
    for word in words:
        if(len(word)>= 3):
            r1 = random_string(3)
            r2 = random_string(3)
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
   
    nwords = []
    for word in words:
        if(len(word)>= 3):
            stnew =  word[3:-3] 
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

