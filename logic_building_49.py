def Anagram(string1, string2):
    dici1 = {}
    dici2 = {}
    for i in string1:
        if i not in dici1:
            dici1[i] = 1
        else:
            dici1[i] +=1
    for i in string2:
        if i not in dici2:
            dici2[i] = 1
        else:
            dici2[i] +=1
    return dici1 == dici2
string1 = "cat"
string2 = "act"
result = Anagram(string1,string2)
if(result):
    print("Anagram")
else:
    print("Not Anagram")