# Print largest word of a sentence
l=list(map(str,input().split(" ")))
stringValue="null"
stringLength=-1
for i in l:
    if len(str(i))>stringLength:
        stringLength=len(str(i))
        stringValue=str(i)
print(stringValue)


