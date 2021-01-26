import os

if __name__ == '__main__':
    tekst = 'Paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

    if  not(os.path.exists("file1.txt")):
        file1 = open("file1.txt", "w+")
    if not (os.path.exists("file2.txt")):
        file2 = open("file2.txt", "w+")
    if not (os.path.exists("file3.txt")):
        file3 = open("file3.txt", "w+")

    for znak in tekst:
        rozmiar1 = os.stat('file1.txt').st_size
        rozmiar2 = os.stat('file2.txt').st_size
        rozmiar3 = os.stat('file3.txt').st_size

        if rozmiar1 < 100:
            file1 = open("file1.txt", "a+")
            if rozmiar1 == 99:
                file2 = open("file2.txt", "w")
            file1.write(znak)
            file1.close()
        elif rozmiar2 < 100:
            file2 = open("file2.txt", "a+")
            if rozmiar2 == 99:
                file3 = open("file3.txt", "w")
            file2.write(znak)
            file2.close()
        elif rozmiar3 < 100:
            file3 = open("file3.txt", "a+")
            if rozmiar3 == 99:
                file1 = open("file1.txt", "w")
            file3.write(znak)
            file3.close()

    print("File1 bytes: ", os.stat('file1.txt').st_size)
    print("File2 bytes: ", os.stat('file2.txt').st_size)
    print("File3 bytes: ", os.stat('file3.txt').st_size)
