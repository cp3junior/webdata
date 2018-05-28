import string
import sys

# Documents are separated by a new line in a text file
with open('doc.txt') as fp:
    documents = fp.read().split("\n")

print("Importing and indexing document...")

# Initialize index dictionary
index = {}


def cleanDoc(str):
    # Transform string into lower case
    str = str.lower()

    # Remove punctuations from string
    table = str.maketrans({key: None for key in string.punctuation})
    str = str.translate(table)

    # Return splited doc
    return str.split(" ")


def searchKeyword(keyword):
    keyword = keyword.lower()
    if keyword in index:
        item = index[keyword]
        freq = item[0]
        docs = ''
        for doc in item[1]:
            docs += doc + " "
        print("The keyword \"" + keyword + "\" appeared " + str(freq) +
              " times in the document. It appeared in " + docs + ".")
    else:
        print("The keyword \"" + keyword + "\" does not exist in the document.")


for i, doc in enumerate(documents):
    doc = cleanDoc(doc)
    for j, word in enumerate(doc):
        currDoc = "D"+str(i+1)
        # Check if the word is already in the index
        if word in index:
            # Increase word frequency
            index[word][0] += 1
            # append the document containing the word if not exist yet
            if currDoc not in index[word][1]:
                index[word][1].append(currDoc)
        else:
            # initialize new word in index
            index[word] = [1, [currDoc]]

while True:
    keyword = input("Input a search keyword (0 to exit): ")
    if keyword == '0':
        print('Exiting ...')
        sys.exit()
    else:
        searchKeyword(keyword)
