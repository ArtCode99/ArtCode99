mess=input("Scrie")
words=mess.split(' ')
emojis={ ":)":"bomba nucleara"}
output=''
for word in words:
    output+=emojis.get(word, word)+' '
print(output)
