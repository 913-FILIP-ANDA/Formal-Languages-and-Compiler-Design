from Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner()

    try:
        st, pif, message = scanner.scanLineByLine("D:/Semestrul 5/compilator/laborator3/inputFiles/p1.txt")
        print("st: ", st)
        print("pif: ", pif)
        print(message)
    except ValueError as ve:
        print(ve)