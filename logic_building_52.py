def remove_special_characters_and_nums(string):
    ans = ""
    for i in range(len(string)):
        if string[i]>="a" and string[i]<="z":
            ans = ans+string[i]
    print(ans)
string = "b#u@g:s:123"
remove_special_characters_and_nums(string)