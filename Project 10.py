import string
def censor():
    filename = input("Enter the filename: ")
    file = open("Censor.txt", 'r').readlines()
    val = open("result.txt", 'w')
    i = 'pizza'
    for i in file:
        words = i.split( )
        for word in words:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 5:
                if "." in word:
                    word = "*****."
                elif "," in word:
                    word = "*****,"
                elif "?" in word:
                    word = "*****?"
                else:
                    word = "*****"
            print(word + " ", file = val, end = "")
    val.close()
censor()
