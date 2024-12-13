from palin import is_pal
def longest_pal(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_pal(s[i:j]) and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest

s = input("Enter a string: ")
print(longest_pal(s))

