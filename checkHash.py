import sys

name_hash = int(sys.argv[1], 16)

print("Hash is " + str(name_hash))

def fieldNameToHash(fieldName):
    ret = 0
    for ch in fieldName:
        ret *= 0x1F
        ret += ord(ch)
        ret &= 0xFFFFFFFF
    return ret

with open("strings.txt", "r", encoding='utf-8') as f:
    data = f.read()
    
for line in data.split("\n"):
    result = fieldNameToHash(line.strip(" "))
    
    if result == name_hash:
        print("Hash matches " + line.strip(" "))
        break

print("Finished.")
