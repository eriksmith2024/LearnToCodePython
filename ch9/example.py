hello = '!?are you there?!'
goodbye = '?fine be that !way!?!!' # strip takes the characters off the end so the !way is still printed

hello = hello.strip('!?')
goodbye = goodbye.strip('!?')

print(hello)
print(goodbye)