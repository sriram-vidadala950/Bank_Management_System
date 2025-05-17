def frequecy_of_character(string):
    dici = {}
    for i in string:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i]+=1
    return dici
string = "sriram"
result = frequecy_of_character(string)
print(result)