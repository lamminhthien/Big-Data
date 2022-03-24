s = 'h\xc6\xb0\xc6\xa1ng'
# Encode to windows-1258 | Vietnamese to keep orginal byte like string
s = s.encode('cp1258')
# Decode to utf-8 with  errors = replace 
print(s.decode("utf-8","replace"))


