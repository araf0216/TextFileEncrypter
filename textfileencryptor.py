Encrypt_Code = {
    'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8', 'D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5', 'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2', 'J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y', 'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v', 'P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's', 'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p', 'V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm', 'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j', '@': 'I', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g', '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd', '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a', ':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<', "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=', '{': '[', '[': '{', '}': ']', ']': '}',
}

def getinpath():
    inpath = input("Enter the path of the text file you would like to encrypt: ")
    if inpath[-4:] != ".txt":
        print("Please choose a text file with the '.txt' extension")
        return getinpath()
    return inpath

inpathverify = ""
while inpathverify.lower() != "y":
    inpath = getinpath()
    inpathverify = input(f"Are you sure '{inpath}' is the correct path to the text file you would like to encrypt? (Y/N): ")

file = open(inpath, "r")

contents = file.read()

encrypted = "".join([Encrypt_Code[char] if char.isspace() == False else char for char in contents])

def getoutpath():
    outpath = input("Please enter the path of the text file to output to: ")
    if outpath[-4:] != ".txt":
        print("Please choose a text file with the '.txt' extension")
        return getoutpath()
    return outpath

outpathverify = ""
while outpathverify.lower() != "y":
    outpath = getoutpath()
    outpathverify = input(f"Are you sure '{outpath}' is the correct path to the text file you would like to write to? (Y/N): ")

with open(outpath, "w") as out:
    out.write(encrypted)
