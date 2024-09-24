# Values-> Series->String
# print indices of a string 



# print with index
string = "salam"
print(len(string))
for i in range (0,len(string)): 
    print(i,string[i])


print("__________________")
# print without any index    
for i in "salam":
    print(i)


    
print("__________________")
#check how many times a letter has been repeated in a string
count = 0
for i in "salam khubam khubi? ":
    if i == "a":
        count+=1
        print(count)
print(len("salam khubam khubi? "))
