def character_compression(string):
    ans = ""
    for i in range(len(string)):
        if string[i].isdigit():
            num = int(string[i])
            ans+=string[i-1]*num
    print(ans)
string = "a32b2c1"
character_compression(string)