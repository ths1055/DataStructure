import random
def genRandList(L,num):
    for i in range(0,num):
        L.append(i)
    random.shuffle(L)

def printListSample(L, num_line, num_sample):
    count=0
    for i in range(num_sample):
        for j in range(num_line):
            print('%7d'%(L[count]),end='')
            count+=1
        print()
    print('......')
    num_printing=num_line*num_sample
    num_len=len(L);num_len-=num_printing
    count=0
    for i in range(num_sample):
        for j in range(num_line):
            print('%7d'%(L[num_len+count]),end='')
            count+=1
        print()
    print()

def shuffleList(L):
    random.shuffle(L)


if __name__=='__main__':
    L=[]
    genRandList(L,100)
    printListSample(L,10,3)
    shuffleList(L)
    printListSample(L,10,3)