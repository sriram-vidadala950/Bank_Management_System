def palindrome_in_range(start,end):
    palindrome = []
    for i in range(start,end+1):
        num = str(i)
        if num == num[::-1]:
            palindrome.append(i)
    print(palindrome)
start = 100
end = 150
palindrome_in_range(start,end)