def convert_num_to_char_using_ascii(string):
    ans = ""
    for i in range(len(string)):
        if string[i].isdigit():
            num = int(string[i])
            ans+=chr(97+num)
        else:
            ans+=string[i]
    print(ans)
string = "a1b2c3"
convert_num_to_char_using_ascii(string)