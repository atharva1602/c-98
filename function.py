def countwords():
    file=input('enter your file name')
    numberofword=0
    filename=open(file,'r')
    for word in filename:
        words=word.split()
        numberofword=numberofword+len(words)
    print(numberofword) 
countwords()
