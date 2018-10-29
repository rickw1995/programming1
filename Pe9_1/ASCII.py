def code(invoerstring):
    encrypted = ""
    for i in invoerstring:
        if i == " ":
            encrypted += "#"
        else:
            encrypted += chr(ord(i)+3)
    return encrypted

print(code("RutteAlkmaarDen Helder"))