#Melanie Dotson
#CSCI 102 - Section D
#Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT',string)

def LoadFile(file):
    mList=[]
    with open(file, 'r') as Afile:
        for line in Afile:
            mList.append(line.rstrip('\n'))

    return mList

def UpdateString(string,new,loc):
    mstring=''
    for i in range(len(string)):
        if i == loc:
            mstring += new
        else:
            mstring += string[i]
    print('OUTPUT',mstring)

def FindWordCount(listi,name):
    C=0
    for i in listi:
        i=i.split()
        for word in i:
            if word == name:
                C+=1
    return C
            
def ScoreFinder(list1,list2,find):
    s=[]
    for i in list1:
        s.append(i.lower())
        
    find=find.lower()
    if find in s:  
        x=s.index(find)
        print('OUTPUT',list2[x])
    else:
        print('OUTPUT player not found')
    
    
def Union(list1,list2):
    return list1+list2

def Intersection(list1,list2):
    mList=[]
    for i in list1:
        if i in list2:
            mList.append(i)
    return mList

def NotIn(list1,list2):
    mList=[]
    for i in list1:
        if i not in list2:
            mList.append(i)
    return mList

