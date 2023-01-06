alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic = { alphabet[i]: alphabet[(i + 13) % 26] for i in range(len(alphabet))}

name = [ dic[k] for k in "CODENAME" ]

print("".join(name))
