s = 'azcbobobegghekl'
#s = 'abcbcd'
currentString = s[0]
longestString = ''
i = 0
for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        currentString = currentString + s[i]
    else:
        if len(currentString) > len(longestString):
            longestString = currentString
        currentString = s[i]
print longestString
            