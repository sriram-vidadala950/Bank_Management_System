def capitalize_each_word(string):
    ans = ""
    for i in range(len(string)):
        if i ==0 or i == len(string)-1 or string[i+1] == " " or string[i-1] == " ":
            st = string[i].upper()
            ans+=st
        else:
            ans+=string[i]
    print(ans)
string = "analyse a book"
capitalize_each_word(string)