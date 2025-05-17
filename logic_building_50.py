def max_repeating_character(string):
    string = string.lower()
    dici = {}
    maxi = 0
    for i in string:
        if i not in dici:
            dici[i] = 1
        else:
            dici[i]+=1
    for key,value in dici.items():
        if value>maxi:
            maxi = value
            max_occur = key
    print(max_occur,maxi)
string = "engineer"
max_repeating_character(string)