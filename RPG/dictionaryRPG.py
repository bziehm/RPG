def DictionaryRPG():
    d={}
    with open (tsvfile.csv) as f:
        for line in f:
            (key,val)=line.split()
            d[int(key)] = val

print (DictionaryRPG)
    
